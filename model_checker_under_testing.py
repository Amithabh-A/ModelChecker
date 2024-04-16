"""
Contains ModelChecker class and model checker testing arena
"""

import copy

from kripkeStructure import KripkeStructure
from node import Node


class ModelChecker:
    """
    Given a Kripke structure K and a CTL formula ϕ, compute the set of states
    Sϕ = { s | s is a state of K and K,s ⊨ ϕ }
    """

    def __init__(self, formula_in_ast: Node, kripke_structure: KripkeStructure) -> None:
        self.formula = formula_in_ast
        self.kripke_structure = kripke_structure
        self.types = {
            "OR": 2,
            "AND": 2,
            "IMP": 2,
            "NOT": 1,
            "EG": 1,
            "EU": 2,
            "EX": 1,
            "VAR": 0,
        }
        self.fill_states(self.formula)

    def postorder_traversal_for_model_checking(self, node: Node) -> None:
        """
        traverse AST in postorder traversal.
        If we are in var node, we will add the states
        that satisfying that proposition and backtrack.
        """
        if self.types[node.type] == 1:
            if node.child is None:
                raise TypeError("node.child's type should be Node, not None")
            self.postorder_traversal_for_model_checking(node.child)
        elif self.types[node.type] == 2:
            if node.left is None:
                raise TypeError("node.child's type should be Node, not None")
            self.postorder_traversal_for_model_checking(node.left)
            if node.right is None:
                raise TypeError("node.right's type should be Node, not None")
            self.postorder_traversal_for_model_checking(node.right)
        self.fill_states(node)

    def fill_states(self, node: Node) -> None:
        """
        fill node.satisfying_state with states that satisfy that node (formula)
        """
        if node.type == "VAR":
            self.fill_var_states(node)
        elif node.type == "OR":
            self.fill_or_states(node)
        elif node.type == "AND":
            self.fill_and_states(node)
        elif node.type == "IMP":
            self.fill_imp_states(node)
        elif node.type == "NOT":
            self.fill_not_states(node)
        elif node.type == "EU":
            self.fill_eu_states(node)
        elif node.type == "EG":
            self.fill_eg_states(node)
        elif node.type == "EX":
            self.fill_ex_states(node)

    def fill_var_states(self, node: Node):
        """
        go over all states of Kripke structure, find states
        that satisfy the proposition of input node
        """
        for state in self.kripke_structure.states:
            if node.child in self.kripke_structure.labelling_function[state]:
                node.satisfying_states.add(state)

    def fill_or_states(self, node: Node) -> None:
        """
        take union of satisfying states of left and right decendents
        """
        if node.left is None:
            raise TypeError("node.left is None, which is not allowed. ")
        if node.right is None:
            raise TypeError("node.right is None, which is not allowed. ")
        node.satisfying_states = (
            node.left.satisfying_states | node.right.satisfying_states
        )

    def fill_and_states(self, node: Node) -> None:
        """
        take intersection of satisfying states of left and right decendents
        """
        if node.left is None:
            raise TypeError("node.left is None, which is not allowed. ")
        if node.right is None:
            raise TypeError("node.right is None, which is not allowed. ")
        node.satisfying_states = (
            node.left.satisfying_states & node.right.satisfying_states
        )

    def fill_not_states(self, node: Node) -> None:
        """
        Find states that does not satisfy the child descendent
        """
        if node.child is None:
            raise TypeError("node.child is None, which is not allowed. ")
        node.satisfying_states = (
            set(self.kripke_structure.states) - node.child.satisfying_states
        )

    def fill_imp_states(self, node: Node) -> None:
        """
        p -> q ≡ ¬p v q
        """
        if node.left is None:
            raise TypeError("node.left is None, which is not allowed. ")
        if node.right is None:
            raise TypeError("node.right is None, which is not allowed. ")
        node.satisfying_states = (
            set(self.kripke_structure.states) - node.left.satisfying_states
        ) | node.right.satisfying_states

    def fill_eu_states(self, node: Node) -> None:
        """
        E [ϕ ∪ Ψ] = Ψ v [ϕ ∧ EX E [ϕ ∪ Ψ]]
        """

        if node.left is None:
            raise TypeError("node.left is None, which is not allowed. ")
        if node.right is None:
            raise TypeError("node.right is None, which is not allowed. ")

        # Initialisation
        node.satisfying_states = copy.deepcopy(node.right.satisfying_states)
        # Repeat
        repeat = True
        while repeat:
            repeat = False
            # for all states s of K :
            for s in self.kripke_structure.states:
                # if s ∈ Sϕ
                if s in node.left.satisfying_states:
                    s_successors = self.kripke_structure.immediate_successor(s)
                    # if atleast one immediate successor s_ of s ∈ S_e ϕ ∪ Ψ
                    for s_ in s_successors:
                        # if s_ in node.satisfying_states
                        if s_ in node.satisfying_states:
                            l = len(node.satisfying_states)
                            node.satisfying_states.add(s_)
                            if l != len(node.satisfying_states):
                                repeat = True

    def fill_eg_states(self, node: Node) -> None:
        """
        EG ϕ = ϕ ∧ EX EG ϕ
        """
        if node.child is None:
            raise TypeError("node.child is None, which is not allowed. ")

        # Initialisation
        # add all states satisfying ϕ in S EG ϕ
        node.satisfying_states = copy.deepcopy(node.child.satisfying_states)
        # repeat
        repeat = True
        while repeat:
            repeat = False
            # for all states s of K:
            for s in self.kripke_structure.states:
                # if s ∈ S EG ϕ
                if s in node.satisfying_states:
                    s_successors = self.kripke_structure.immediate_successor(s)
                    # If no successors s_ ∈ S EG ϕ, remove s from S EG ϕ
                    for s_ in s_successors:
                        # if s_ in S EGϕ, nothing to remove. break from loop
                        if s_ in node.satisfying_states:
                            break
                    else:
                        node.satisfying_states.remove(s)

    def fill_ex_states(self, node: Node) -> None:
        """
        EX ϕ
        """

        if node.child is None:
            raise TypeError("node.child is None, which is not allowed. ")

        # for all states s of K
        for s in self.kripke_structure.states:
            # if ∃ s' st s' ∈ Sϕ, add s to S EX ϕ
            s_successors = self.kripke_structure.immediate_successor(s)
            for s_ in s_successors:
                if s_ in node.child.satisfying_states:
                    node.satisfying_states.add(s)
                    break

"""
Contains ModelChecker class and model checker testing arena
"""

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

    def postorder_traversal_for_model_checking(self, node: Node) -> None:
        """
        traverse AST in postorder traversal.
        If we are in var node, we will add the states that satisfying that proposition and backtrack.
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
        if node.type == "VAR":
            self.fill_var_states(node)

    def fill_var_states(self, node: Node):
        pass

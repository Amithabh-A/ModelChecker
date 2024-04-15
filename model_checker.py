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

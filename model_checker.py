"""
Contains ModelChecker class and model checker testing arena
"""


class ModelChecker:
    def __init__(self, formula_in_ast, kripke_structure) -> None:
        self.formula = formula_in_ast
        self.kripke_structure = kripke_structure

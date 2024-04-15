"""
Contains ModelChecker class and model checker testing arena
"""

from converter import parser


class ModelChecker:
    def __init__(self, kripke_structure, formula):
        self.formula = formula
        self.kripke_structure = kripke_structure


def parse_input(s):
    return parser.parse(s)


# Example usage
input_string = input("Input formula : ")
ast = parse_input(input_string)

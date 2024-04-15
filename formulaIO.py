from converter import parser
from node import Node


class FormulaParser:
    def __init__(self, formula_parser, formula) -> None:
        self.parser = formula_parser
        self.formula = formula
        self.parse_input()

    def parse_input(self):
        self.ast = Node(parser.parse(self.formula))


s = input("Input formula : ")
f = FormulaParser(parser, s)

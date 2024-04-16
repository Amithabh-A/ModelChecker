"""
class definition for formula input and parse
"""

from converter import parser
from node import Node


class Formula:
    def __init__(self, formula_parser=parser) -> None:
        self.parser = formula_parser
        self.formula = input("Input formula : ")
        self.parse()

    def parse(self):
        """
        parse formula using (input) parser
        """
        self.ast = Node(parser.parse(self.formula))

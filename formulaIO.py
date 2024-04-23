"""
class definition for formula input and parse
"""

from converter import parser
from node import Node


class Formula:
    def __init__(self, formula_parser=parser) -> None:
        self.parser = formula_parser
        # self.formula = input("Input formula : ")
        self.formula = input()
        self.parse()
        self.show()

    def parse(self) -> Node:
        """
        parse formula using (input) parser
        """
        self.parser_out = self.parser.parse(self.formula)
        self.ast = Node(self.parser_out)
        return self.ast

    def show(self):
        """
        Output the resultant formula in EG, EU and EX representation
        output number of nodes in parse tree
        In the bottom-up order, for each node of parse tree, output node-id and
        subformula corr. to that node.
        """
        print(f"resultant formula : {self.parser_out}")
        print(f"No of Nodes : {self.ast.node_count-1}")
        self.bottom_up_traversal(self.parser_out)

    def bottom_up_traversal(self, t: tuple):
        """
        bottom up traversal of parse tree
        uses parser_out
        """
        if len(t) == 2:
            if isinstance(t[1], tuple):
                self.bottom_up_traversal(t[1])
            print(f"Node Id : {t[0]}\tSubformula : {t}")
        elif len(t) == 3:
            if isinstance(t[1], tuple):
                self.bottom_up_traversal(t[1])
            if isinstance(t[2], tuple):
                self.bottom_up_traversal(t[2])
            print(f"Node Id : {t[0]}\tSubformula : {t}")
        elif len(t) == 1:
            print(f"Node Id : {t[0]}")


# f = Formula().parse()
# f.inorder_traversal()

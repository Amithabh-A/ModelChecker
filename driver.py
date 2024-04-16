from formulaIO import Formula
from kripkeStructure import KripkeStructure
from model_checker import ModelChecker

K = KripkeStructure()
f = Formula().parse()
MC = ModelChecker(f, K)
print(MC.formula.satisfying_states)
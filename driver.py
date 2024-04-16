from formulaIO import Formula
from kripkeStructure import KripkeStructure
from model_checker import ModelChecker

K = KripkeStructure()
formula = Formula()

MC = ModelChecker(formula.ast, K)
print(MC.formula.satisfying_states)

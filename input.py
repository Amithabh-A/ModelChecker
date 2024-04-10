"""
input module. 
"""

from kripkeStructure import KripkeStructure

ks = KripkeStructure()

n = int(input("Input no of states : "))
ks.set_len_of_states(n)

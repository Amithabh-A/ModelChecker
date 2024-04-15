Programming language : Python

Input :
A kripke structure :
set of atomic propositions -- p1, p2, ...
K is a directed graph with a labelling function

A fully paranthesized CTL formula ϕ

Procedure :
Step 1 :
convert formula ϕ into equivalent set Ψ having convenient set of CTL formula used.
a. o/p resultant formula Ψ
b. output no of nodes
c. In bottom-up order for each node of parse tree, o/p node-id and subformula corr to tht node.
d. store parse tree of Ψ for later processing

Step 2 :
Implement bottom-up model checking algo tht outputs subsets of states of K tht satisfies Ψ
choose an appropriate ds for fast lookup.

Note :
given K and a ctl formula ϕ, compute Sϕ = { s | s is a state of K, K,s ⊨ ϕ }

conversion of ϕ to Ψ
Formula :

AG EG
AF EF
AU EU
AX EX
v ∧ ¬ ->

set of CTL formula used : EG EU EX

types : OR, AND, NOT, IMP, EG, EU, EX

AG -> EF EG
AF -> EG EF -> EU
AU -> AF -> EG EU
AX -> EX EX

('AG', ('VAR', 'f')) - ('NOT', ('EF', ('NOT', f)))

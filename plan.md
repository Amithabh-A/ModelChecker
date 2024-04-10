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

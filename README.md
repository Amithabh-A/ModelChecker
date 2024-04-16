# CTL(Computational Tree Logic) Model Checker

This is a simple CTL model checker implemented in Python. The repo consist of the following : 
* A CTL formula parser `parser.py`
* Yet Another CTL formula parser `converter.py` which generate AST where type nodes are only the temporal operators {EX, EG, EU}
* Model Checker class in `model_checker.py ` module
* Kripke structure class in `kripkeStructure.py`
* write other stuffs...

You can specify your Kripke structure and formula in `input.txt`. The guidelines for how to fill `input.txt` is been instructed in `manual.txt`. 

# How to use
Clone this repository into your local machine. 
```
git clone git@github.com:Amithabh-A/ModelChecker.git
```
run make command
```
make
```
activate the environment
```
source venv/bin/activate
```
run Model Checker using Kripke structure and formula mentioned in `input.txt`
```
make run
```

# Contributions
I would like you to fix `Makefile` firstly :)

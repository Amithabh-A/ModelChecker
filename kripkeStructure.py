class KripkeStructure:
    """
    Creates a Kripke Structure
    """

    def __init__(self):
        self.n = 0
        """
        states S
        """
        self.states = list[int]
        """
        start states S_0
        """
        self.start_states = list[int]
        """
        transitions δ ⊆ S x S 
        """
        self.transitions = []  # list[tuple[int, int]]
        """
        propositions AP store all propositional variables of Kripke Structure 
        """
        self.propositions = list[str]
        """
        labelling function LS  for each state 
        """
        self.labelling_function = {}  # dict[int, list[str]]

        # setup
        self.setup()

    def set_states(self):
        """
        get n and set states as 1,...,n
        """
        if self.n == 0:
            n = int(input("Input no of states : "))
            self.n = n
        else:
            print("state length already set!")
        self.states = list(range(1, self.n + 1))

    def set_start_states(self):
        """
        start states of kripke structure.
        """
        self.start_states = list(
            map(int, input("input start states of kripke structure : ").split())
        )

    def set_propositions(self):
        """
        AP of kripke structure
        """
        self.propositions = list(
            input("input propositions of kripke structure : ").split()
        )

    def set_transitions(self):
        """
        transitions of kripke structure.
        """
        while True:
            try:
                s, e = map(int, input("transitions: ").split())
                self.transitions.append((s, e))
            except EOFError:
                print()
                break

    def set_labels(self):
        """
        labels of each state
        """
        for s in range(1, self.n + 1):
            ls = input(f"labels of state {s}: ").split()
            self.labelling_function[s] = ls

    def setup(self):
        self.set_states()
        self.set_start_states()
        self.set_transitions()
        self.set_propositions()
        self.set_labels()

    def show(self):
        print(self.states)
        print(self.start_states)
        print(self.transitions)
        print(self.propositions)
        print(self.labelling_function)

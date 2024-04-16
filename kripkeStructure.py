class KripkeStructure:
    """
    Creates a Kripke Structure
    """

    def __init__(self):
        self.n = 0
        """
        states S
        """
        self.states: set[int] = set()  # list[int]
        """
        start states S_0
        """
        self.start_states: set[int] = set()
        """
        transitions δ ⊆ S x S 
        """
        self.transitions: set[tuple[int, int]] = set()  # list[tuple[int, int]]
        """
        propositions AP store all propositional variables of Kripke Structure 
        """
        self.propositions: set[str] = set()
        """
        labelling function LS  for each state 
        """
        self.labelling_function: dict[int, set[str]] = {}  # dict[int, list[str]]

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
        # self.states = set(list(range(1, self.n + 1)))
        self.states = set(range(1, self.n + 1))

    def set_start_states(self):
        """
        start states of kripke structure.
        """
        self.start_states = set(
            list(map(int, input("input start states of kripke structure : ").split()))
        )

    def set_propositions(self):
        """
        AP of kripke structure
        """
        self.propositions = set(
            list(input("input propositions of kripke structure : ").split())
        )

    def set_transitions(self):
        """
        transitions of kripke structure.
        """
        while True:
            try:
                s, e = map(int, input("transitions: ").split())
                self.transitions.add((s, e))
            except EOFError:
                print()
                break

    def set_labels(self):
        """
        labels of each state
        """
        for s in range(1, self.n + 1):
            ls = set(input(f"labels of state {s}: ").split())
            self.labelling_function[s] = ls

    def setup(self):
        self.set_states()
        self.set_start_states()
        self.set_transitions()
        self.set_propositions()
        self.set_labels()

    def immediate_successor(self, state: int) -> set:
        return {e for s, e in self.transitions if s == state}

    def show(self):
        print(self.states)
        print(self.start_states)
        print(self.transitions)
        print(self.propositions)
        print(self.labelling_function)

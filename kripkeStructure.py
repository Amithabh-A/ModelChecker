class KripkeStructure:
    def __init__(self):
        self.n = 0
        self.states = []
        self.start_states = []
        self.propositions = []
        self.transitions = dict[tuple[int, int], set[str]]

        self.set_states()
        self.set_propositions()

    def set_states(self):
        """
        get no of states of kripke structure and set states.
        """
        if self.n == 0:
            n = int(input("Input no of states : "))
            self.n = n
        else:
            print("state length already set!")
        self.states = list(range(1, self.n + 1))

    def set_start_states(self):
        """
        get start states of kripke structure.
        """
        self.start_states = list(
            map(int, input("input start states of kripke structure : ").split())
        )

    def set_propositions(self):
        """
        set states of kripke structure
        """
        self.propositions = list(
            input("input propositions of kripke structure : ").split()
        )

    def set_transitions(self):
        """
        set transitions of kripke structure.
        """
        while True:
            s, e = map(int, input("input transition :").split())
            self.transitions.add((s, e))

class State:
    """A state in automaton."""
    def __init__(self, accept, arrows):
        #True if this is an accept state.
        self.accept = accept
        #Arrows (keys are labels) out of state.
        self.arrows = arrows

class DFA:
    """An Automaton"""
    def __init__(self, start):
        #Start state of the automation
        self.start = start

    def match(self, s):
        """See if s is accepted by automaton"""
        # Currrent state
        current = self.start
        #loop through the characters in s.
        for c in s:
            # Find the state in arrows with key c.
            current = current.arrows[c]
         # Return whethere we're in an accept state.
        return current.accept

def compile():
    """Create the automaton."""

    # Create the start state.
    start = State(True, {})

    #Creataing other stae
    other = State(False, {})

    # the states point to themselves on a 0.
    start.arrows['0'] = start
    other.arrows['0'] = other

    #The states point to each other on a 1.
    start.arrows['1'] = other
    other.arrows['1'] = start

    # cReate an automaton
    parity = DFA(start)

    #return automaton.
    return parity

# create automaton instance
myautomaton = compile()
for s in ['1100', '11111', '', '1', '0']:
    # check if s is accepted by the automaton
    result = myautomaton.match(s)
    # print result
    print(f"{s} -> {result}")

for s in ['000', '001', '010', '011', '100', '101', '110', '111']:
    # check if s is accepted by the automaton
    result = myautomaton.match(s)
    # print result
    print(f"{s} -> {result}")

    #few tests, create automaton, loop through list of strings,
    #1100 = match
    #11111 = not match
    #'' = match
    #1 = not
    #0 = match

    #s is each string, stored in variable called result
    #f means formatted strings


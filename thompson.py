# Thompson's Construction

class State():
    """A state and its arrows in Thompson's construction."""
    #  # A label. None if e.
    #  label = None
    #  # Next states after this one..
    #  arrows = []
    #  # Is this an accept state?
    #  accept = False
    # Constructor.
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of state to point to, is a boolean as to whether 
        this is an accept state"""
        self.label = label
        self.arrpws = arrows
        self.accept = accept

class NFA:
    """A non-deterministic finite automaton."""
    # # start state.
    # start = None
    # # End state
    # end = None
    def __init__(self, start, end):
        self.start = start
        self.end = end

def re_to_nfa(postfix):
    #a stack for NFAs
    stack = []
    # Loop through the postfix r.e left to right.
    for c in postfix:
        # Concatenation
        if c == '.':
            # pop top NFA off stack.
            nfa2 = stack [-1]
            stack = stack[:-1]
            #Pop the next NFA off stack.
            nfa1 = stack [-1]
            stack = stack [:-1]
            # Make accept state of NFA1 non-accept
            nfa1.end.Accept = False
            # make it point at start state of nfa2
            nfa1.end.arrows = [nfa2.start]
            # Make a new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(start=nfa1.start, end=nfa2.end)
            # push to the stack.
            stack.append(nfa)

        elif c == '|':
            # pop top NFA off stack.
            nfa2 = stack [-1]
            stack = stack[:-1]
            #Pop the next NFA off stack.
            nfa1 = stack [-1]
            stack = stack [:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            #make old accept states non-accept
            nfa1.end.Accept = False
            nfa2.end.Accept = False
            # Make a new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(start, end)
            # push to the stack.
            stack.append(nfa)
        elif c == '*':
             # pop one NFA off stack.
            nfa1 = stack [-1]
            stack = stack[:-1]
            # Create new start and end states
            start = State(None, [], False)
            end = State(None, [], True)
            # make new start state point at old start states
            start.arrows.append(nfa1.start)
            # and at the new end state
            start.arrows.append(end)
            #make old accept states non-accept
            nfa1.end.Accept = False
            #make old accept state point to new accept state
            nfa1.end.arrows.append(end)
            #make old accept state point to old accept state
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(start, end)
            # push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-character 'c'
             #Create the end state.
            end = State(label=None, arrows=[], accept=True)
            # create the start state, pointed at the end state.
            start = State(label = c, arrows=[end], accept = False)
            #Create the NFA with the start and end state
            nfa = NFA(start=start, end=end)
            # append the NFA to the NFA stack
            stack.append(nfa)

    # there should only be one NFA on the stack.
    return stack[0]

if __name__ == "__main__":
    for postfix in ["abb.*.a .", "100.*.1."]:
        print(f"postfix:  {postfix}")
        print(f"nfa:      {re_to_nfa(postfix)}")
        print()

           
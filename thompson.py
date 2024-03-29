# Thompson's Construction

class State:
    """A state and its arrows in Thompson's construction."""
    #  # A label. None if e.
    #  label = None
    #  # Next states after this one..
    #  arrows = []
    #  # Is this an accept state?
    #  accept = False
    # Constructor.
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of state to point to,
        is a boolean as to whether 
        this is an accept state"""
        self.label = label
        self.arrows = arrows
        self.accept = accept

    def followes(self):
        """The set of states that are gotten from following this state and all
        its e arrows."""
        #include this state in the returned set.
        states = {self}
        # if this state has e arrows, i.e label is None.
        if self.label is None:
            #loop through this state's arrows
            for state in self.arrows:
                #Incorporate that state's e arrow states in states
                states = (states | state.followes())
        return states
    

class NFA:
    """A non-deterministic finite automaton."""
    # # start state.
    # start = None
    # # End state
    # end = None
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):
        """Return True iff this NFA (instance) matches the string s."""
        #List of previous states that we are still in 
        previous = self.start.followes()
        #loop through string, a character at a time.
        for c in s:
            # start with an empty set of current states.
            current = set()
            #loop through the previous states.
            for state in previous:
                # Check if there is a c arrow from state.
                if state.label == c: 
                    # addd followes for next state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current.
            previous = current
        #if the final state is in previous, then return True. False otherwise
        return (self.end in previous)
        
        # Test: print no of states ^
      #  # ## follow the e arrows for each of the current states.
       # for state in current:
        #     #states with e arrows have None as their label
        #     if state.label is None:
        #         # Append all future states.
        #         current = (current | set(state.arrows))
        #print(f"No of states we're in: {len(current)}")

def re_to_nfa(postfix):
    #a stack for NFAs
    stack = []
    # Loop through the postfix r.e left to right.
    for c in postfix:
        # Concatenation
        if c == '.':
            # pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            #Pop the next NFA off stack.
            nfa1 = stack [-1]
            stack = stack [:-1]
            # Make accept state of NFA1 non-accept
            nfa1.end.accept = False
            # make it point at start state of nfa2
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state
            nfa = NFA(nfa1.start, nfa2.end)
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
            nfa1.end.accept = False
            nfa2.end.accept = False
            #point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # make a new NFA
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
            nfa1.end.accept = False
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
            # point new start state at new end sttate
            start.arrows.append(end)
            #Create the NFA with the start and end state
            nfa = NFA(start=start, end=end)
            # append the NFA to the NFA stack
            stack.append(nfa)

# there should only be one NFA on the stack.
    if len(stack) != 1:
        return None
    else:
        return stack[0]

if __name__ == "__main__":
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|', "a*"]:
        print(f"postfix:  {postfix}")
        print(f"nfa:      {re_to_nfa(postfix)}")
        print()

           
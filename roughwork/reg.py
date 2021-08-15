import shuntingre
import thompson

#with open('file.txt', 'r') as f:
    # Read a line of f.
    # See if it matches the regualr expression.
    # If it does, print the line 

#Extra Marks
# a*: zero or more a's
# a+: one or more a's i.ie aa*
# add another elif to thompson.py that allows special character + to be used where similar 
#to *,concatinate Kleene star

if __name__ == "__main__":
    tests = [    ["(a.b|b*)",["ab", "b", "bb", "a"]]
               , ["a.(b.b).a*",["aa", "abba", "aba"]]
               , [ "1.(0.0)*.1", ["11", "100001", "11001"]]
    ]

    for test in tests:
        infix = test[0]
        print(f"infix:  {infix}")
        postfix = shuntingre.shunt(infix)
        print(f"postfix: {postfix}")
        nfa = thompson.re_to_nfa(postfix)
        print(f"thompson: {nfa}")
        for s in test[1]:
            match = nfa.match(s)
            print(f"Match '{s}': {nfa.match(s)}")
        print()

           
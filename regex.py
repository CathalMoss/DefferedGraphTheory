import re

myre = re.compile('a+b+')

examples = ['ab', 'aab', 'abb', 'aaabbb', 'ca', 'abab']

for e in examples:
    if myre.match(e):
        ismatch = True
    else:
     ismatch = False
    print(f"{e}->{ismatch}")

#example of deffered project
myre2 = re.compile('cab')
counter = 0

examples = ['fab', 'cab', 'dab', 'cat']

for e in examples:
    if myre2.match(e):
        ismatch = True
        counter+=1
    else:
     ismatch = False
    print(f"{e}->{ismatch}")
print(f"There is {counter} answer(s) related to cab")
#got counter working which would be benefical to project

#example3 
#tried several different operators for this and couldn't get the correct answer
myre3 = re.compile('a&b')
counter = 0

examples = ['fab', 'cab', 'dab', 'cat'] 

for e in examples:
    if myre3.match(e):
        ismatch = True
        counter+=1
    else:
     ismatch = False
    print(f"{e}->{ismatch}")
print(f"There is {counter} answer(s) related to cab")

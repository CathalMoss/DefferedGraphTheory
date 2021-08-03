# Cathal Moss
#Python basics
#2021-07-27

print("Hello World!")

a =1
b= 1.0
s = "Hello, world from a string!"
t = '"Hello" from a different string'
#u = "\"Hello\", world!"

print(a, b, s, t)

print(type(a))

print(s[1])

#slice
# print(s[3:10:2])
#start at 3 end at char 10 and skip two everytime
# s[5:2]

# for (i = 1; i < 5; i+=2)
# s[i]

x = [1,2,3, "Hello", 1.0]
# print(x)
# print(x[0])
# print(x[2])
# print(x[-1])

for i in x[0::2]:
    print(i)
    #concatinates when string
    print(i+i)

#loop through set of integers
for i in range(11):
    print(i)

#name is no_wheels/element
d = {"no_wheels": 4, "make": "Skoda"}

print(d["no_wheels"])
# print(d["make"])

d["model"] = "Superb"
print(d["model"])

r = [1,2,3,4]
print(r)
s= [i*i for i in r]
print(s)

def factorial(n):
    """Number to calculate factorial of."""
    if n < 1:
        m = -n
    else:
        m = n
    # the running total - eentuallt rhe factorial.
    total = 1
    #copy the value
    # m = n
    # Loop to do the multiplications.
    while m >0:
        total = total * m
        m = m -1

    #retirn the answer
    if n < 1:
        return - total
    else:
        return total
    
#test the function
n = -20
#calculate the factorial of n.
print(f"The factorial of {n} is {factorial(n)}.")


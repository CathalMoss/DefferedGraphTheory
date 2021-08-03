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
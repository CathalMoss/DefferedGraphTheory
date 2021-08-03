"""Verifiying the Collatz Conjecture."""

#Cathal Moss
#03-08-21

def f(n):
    # if n is even.
    if n % 2 == 0:
        #// = interger division / = floating point division
        return n // 2
    # if n is odd.
    elif n % 2 == 1:
        return (3 * n ) + 1
    else:
        return None

def collatz(n):
    so_far = []
    #loop unril n is 1.
    while n != 1:
        if n in so_far:
            return False
        so_far.append(n)
        n= f(n)
    so_far.append(n)
    return so_far

# print(collatz(10))
# print(collatz(27))
print(collatz(1234567))
"""
R-1.1
Write a short Python function, is multiple(n, m), 
that takes two integer values and returns True if n is a multiple of m, 
that is,n = mi for some integer i, andFalse otherwise
"""

def is_multiple(n,m):
    return True if n%m == 0
    
    
"""
R-1.2 Write a short Python function, is even(k), that takes an integer value and 
returns True if k is even, and False otherwise. However, 
your function cannot use the multiplication, modulo, or division operators
"""

def is_even(k):
    return True if k in range(0,k+1,2) else False
    
"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
and returns the smallest and largest numbers, in the form of a tuple of length two. 
Do not use the built-in functions min or max in implementing your solution. 
"""

def minmax(*args):
    
    inp_list =[]
    for num in args:
        inp_list.append(num)
    inp_list.sort()
    inp_list = inp_list[0], inp_list[len(inp_list)-1]
    return inp_list



"""
R-1.4 Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller than n. 
"""

def sum_squares(n):
    sum_s = 0
    for i in range (0, n):
        sum_s += i**2
    return sum_s

#1 liner solution bellow!

"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, 
relying on Python’s comprehension syntax andthe built-in sum function.
"""

def sum_squares2(n):
    return sum([i**2 for i in range (0,n)])


"""
R-1.6 Write a short Python function that takes a positive integer n and 
returns the sum of the squares of all the odd positive integers smaller than n.
"""
#This is answer for R-1.7 as well
def sum_sqares_odd(n):
    return sum([i**2 for i in range (0,n) if i%2 == 1])

"""
R-1.8 Python allows negative integers to be used as indices into a sequence, such as a string. 
If string s has length n, and expression s[k] is used for index−n≤k<0, what is the equivalent 
index j≥0such thats[j]references the same element? 
"""

equiv_index = lambda string, neg_k: len(string) + neg_k

# R-1.9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80? 
#in order to see this as a list:

list(range(50,81,10))

"""
R-1.10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0,−2,−4,−6,−8?
"""
list(range(8,-9,-2))

"""
R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]. 
"""

#this is the solution asked

[2**i for i in range(9))]

#other solutions
s = [1]
x = 1
for i in range(8):
    x = x*2
    s.append(x)
print(s)

x = 1
lst = [1]
while x < 129:
    x += x
    lst.append(x)
print(lst)

"""
R-1.12 Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
The random module includes a more basic function randrange, with parameterization similar to the built-in range function, 
that return a random choice from the given range. Using only the randrange function, implement your own version of 
the choice function
"""
#normaly we would have to import random at the begin of the code, in this case though I act as it's problem-solution is seperate
#also normally we would have to put this """ explenation """ bellow the definition of its' function. 

import random
def randomchoice(data):
    
    """
    we use this space to explain the function
    """

    return random.choice(data)

#you can test this with any given list, e.g: 

yolo = [1,3,5,"a", 8, "32"]

#then run it:
# randomchoice(yolo)

#enjoy!!! 

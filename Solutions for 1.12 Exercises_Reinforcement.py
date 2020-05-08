"""
R-1.1
Write a short Python function, is multiple(n, m), 
that takes two integer values and returns True if n is a multiple of m, 
that is,n = mi for some integer i, andFalse otherwise
"""

def is_multiple(n,m):
    return True if n%m == 0 else False
    
    
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

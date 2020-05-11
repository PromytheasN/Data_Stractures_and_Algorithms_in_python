"""
C-1.13 
 Write a pseudo-code description of a function that reverses a list of n integers, 
 so that the numbers are listed in the opposite order than they were before, 
 and compare this method to an equivalent Python function for doing the same thing
"""
 
#There is multiple ways to do this. The simplest one would be to reverse the list by using this methodology:
liss1 = [1,2,3,4,5,6,7,8]

"""
From my understanding what we do here is that we take all the index values of the list starting from the benin
of the list, and then we go a step backwards instead of a step forward. That way the new reversed list will begin
from the first index value without including it, and move backwords from the end towards the begining of the original
list, effectively reversing it.
"""

rev_liss1 = liss [::-1]

"""
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose product is odd. 
"""

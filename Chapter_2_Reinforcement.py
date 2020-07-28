"""
R-2.1 Give three examples of life-critical software applications.
"""
#1) Critical life support machine software
#2) Auto-drive (for self drive vehicles) software
#3) Nuclear reactors software

"""
R-2.2 Give an example of a software application in which adaptability can mean
the difference between a prolonged lifetime of sales and bankruptcy.
"""
#Any trademarked Operating System (eg. Windows)

"""
R-2.3 Describe a component from a text-editor GUI and the methods that it encapsulates.
"""




"""
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type
"""
class Flower:
    
    def __init__(self):
        
        #Defining variables
        self.name = ""
        self.petal_num = 0
        self.price = 0.0
        
        
    def get_name(self):
        return self.name
        
    def get_petal_num(self):
        return self.petal_num
    
    def get_price(self):
        return self.price
    
    def set_name(self, name):
        self.name = name
        
    def set_petal_num(self, petal_num):
        self.petal_num = petal_num
        
    def set_price(self, price):
        self.price = price
    
        
      
"""
R-2.5 Use the techniques of Section 1.7 to revise the charge and make_payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter
"""

class CreditCard:
    """A consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        the initial balance is zero
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)"""
        
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    
    def get_bank(self):
        """return the banks name"""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self,price):
        """ Charge given price to the card, assuming sufficient credit limit.
        return True if chage was processed; False if charge was denied."""
        
        try:
            if price + self._balance > self._limit: #If charge would exceed limit,
                return "Transaction Error, inceficient funds."
            else:
                self._balance += price
                return "Thank you for your transaction!"
        except:
            return "Looks like there was an error with this charge. Please attempt to charge the card only in USD"
        
        #lse:
            #eturn 
    def make_payment(self, amount):
        """Checks if input is valid and process customer payment that reduces balance"""
        try:
            self._balance -= amount
        except:
            return "Looks like that you haven't input a numeric amount"
        
        else:
            return "Thank you for your payment!"
        
        
"""
R-2.6 If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""

def make_payment(self, amount):
    """Checks if input is valid and process customer payment that reduces balance"""
    try:
        #Add on, checks if payable amount is positive
        if amount >= 0:
            self._balance -= amount
        #If no possitive, returns VallueError
        else:
            return "ValueError"
    except:
        return "Looks like that you haven't input a numeric amount"

    else:
        return "Thank you for your payment!"

    
"""R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero. 
Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance."""

class CreditCard:
    """A consumer credit card."""
    
    #We added balance = 0 as an optional input, if there is none then balance = 0
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """Create a new credit card instance.
        the initial balance is zero
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)"""
        
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        #We shifted self._balance = balance incase there is an input
        self._balance = balance    


        
"""R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?"""        
#Unittest

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Bowman", "California Savings",
                             "5391 0375 9387 5309", 2500))
    wallet.append(CreditCard("John Bowman", "California Federal",
                            "3485 0399 3395 1954", 3500))
    wallet.append(CreditCard("John Bowman","California Finance",
                            "5391 9375 9387 4309", 5000))
    
    for val in range(1,17):
      wallet[0].charge(val)
      wallet[1].charge(2*val)
    #we change the charge from 3*val to 3333*val so the card exceeds limit
      wallet[2].charge(3333*val)
                  
    for c in range(3):
        print('Customer = ' , wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ' , wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()   
        
        
        
"""R-2.9 Implement the __sub__ method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors."""

class Vector:
    """Represent a vector in multidimensional space."""
    
    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0]*d
        
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
    
    def __getitem__(self,j):
        """Return the coordinate of vector."""
        return self._coords[j]
        
    def __setitem__(self, j , val):
        """Set the coodrinate of vector to given value."""
        self._coords[j] = val
    
    #Here we add the __sub__ method as requested so we can add Vectors
    def __sub__(self, other):
        """Return sub of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree!")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result    
        
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): #relies on __len__ method
            raise ValueError("dimensions must agree!")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other #rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vector"""
        return "<" + str(self._coords)[1:-1] + ">" # adapt list representation        

"""R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v."""

    #This should be added in class Vector:
    def __neg__(self):
       """Return new Vector instance whose coordinates are all negated values of the original ones"""
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] *= -1
        return result
    
   
"""
R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
"""

    #We add this function to our Vector class
    def __radd__(self, other):
        """Returns Vectors sum with other coordinates of object with same dimentions"""
        return self.__add__(other)


"""R-2.12 Implement the __mul__ method for the Vector class of Section 2.3.3, so
that the expression v*3 returns a new vector with coordinates that are 3
times the respective coordinates of v."""


    def __mul__(self, other):
        """Return new Vector instance whose coordinates are x(other) times of the original"""
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] *= other
        return result
    
    
  """R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v*3. Implement
the rmul method, to provide additional support for syntax 3*v."""

    def __rmul__(self, other):
        """Return new vector instance whose coordinates are x times of the original with the first factor being an x value and second the Vector"""
        return self.__mul__(other)

"""R-2.14 Implement the __mul__ method for the Vector class of Section 2.3.3, so
that the expression u*v returns a scalar that represents the dot product of
the vectors, that is, ∑d
i=1 ui · vi."""

    def __mul__(self, other):
        """Return a scalar that represents the dot product of 2 vectors"""
        result = Vector(len(self)) + self
        for i in range(len(self)):
            result[i] = result[i] * other[i]
        return result

    
 """R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence."""

#We modifie __init__ to this:
    def __init__(self, d):
        """Create d-dimensional vector of zeros or of certain dimentional coordinates"""
        try:
            if int(d):
                self._coords = [0]*d
        except:
            if list(d):
                self._coords = d
                
                
"""R-2.16 Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop − start + step − 1) // step)
to compute the number of elements in the range. It is not immediately evident why this formula provides the correct calculation, even if assuming
a positive step size. Justify this formula, in your own words."""

"""From this equation we have the last number minus the first one to find the total difference. Then we also add the step in order to include the
first number of our len(range(x,y)) but we do -1 as well in order to make sure that we are not including the last number y, in our len. after we find
the difference we divide it by the stp in order to find the total amount of steps within this range(x,y,s)""" 



"""R-2.18 Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values."""

class Progression:
    """Iterator produicing a generic progression.
    Default iterator producces the whole numbers 0,1,2,..."""
    
    def __init__(self,start=0):
        
        """Initialize current to the first value of the progression."""
        self._current = start
        
    def _advance(self):
        """Update self._current to a new value.

        This shouldd be overriden by a subclass to customize progression.
        By convention, if current is set to None, this desigantes the end of 
        a finite progression"""

        self._current += 1
        
    def __next__(self):
        
        """Return the next element, or else raise StopIteration error."""
        
        if self._current is None: #our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current #record current value to return
            self._advance() #advance to prepare for next time
            return answer #return the answer
        
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
    def print_progression(self,n):
        """Print next n values of the progression."""
        print(" ".join(str(next(self))for j in range(n)))
        
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    
    def __init__(self, first = 0, second = 1):
        """Create a new fibonacci progression.
        
        first the first term of the progression(default 0)
        second the second term of progression(default 1)
        """
        
        super().__init__(first) #starts progression at first
        self._prev = second - first #fictious value preceding the first
        
    def _advance(self):
        """Update current value by taking sum of previous two."""
        
        self._prev, self._current = self._current, self._prev + self._current
        
#This code will produce the fibonacci progression up to 8th value starting with 2 and 2
FibonacciProgression(2,2).print_progression(8)

        

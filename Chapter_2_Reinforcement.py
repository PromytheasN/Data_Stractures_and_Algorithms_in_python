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

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
    
    def __init__(self, name, petal_num, price):
        
        #Defining variables
        self.name = name
        self.petal_num = petal_num
        self.price = price
        
    
    def __str__(self):
        
        #Retrieving values.
        return f"{self.name} flower has {self.petal_num} petals and cost ${self.price}"
    
        
      
"""
R-2.5 Use the techniques of Section 1.7 to revise the charge and make_payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter
"""

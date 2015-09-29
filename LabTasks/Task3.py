__author__ = 'Vladislav'


# Function in Python language.
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Entering data.
first = input("Enter first number: ")
second = input("Enter second number: ")

# Demonstrating how find_max works!
print "Maximum is: "+ str(find_max(first, second))
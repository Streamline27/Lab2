__author__ = 'Vladislav'


# Some types in python are mutable some are not.
# this is the only way to change variable inside function.
def mutable_pow(a):
    a[0] **= 2
    print "Inside mut_pow "+ str(a[0])


# In this way variable wont be mutated
# but will be returned.
#  This is a nice way to go!
def function_pow(a):
    a **= 2
    print "Inside function_pow " + str(a)
    return a**2


# Entering data
i = input("Enter number: ")

# Demo of call by value
function_pow(i)
print "After by value: "+str(i)

# Demo of only way to mutate passed int
mutable_list = [i]
mutable_pow(mutable_list)
print "After by list: "+ str(mutable_list[0])
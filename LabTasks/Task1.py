import random

__author__ = 'Vladislav'

# Entering domain elements
print "Enter count of numbers in domain:",
numDomain = input()
domain_for_randoms = []
for i in range(0, numDomain):
    domain_for_randoms.append(input())

# Entering number of elements in list of random numbers
print "Enter number of elements:",
numElements = input()

# Generating list of random elements from supplied domain.
randoms = []
for i in range(0, numElements):
    randoms.append(random.choice(domain_for_randoms))

# Displaying elements in 8 columns
for i in range(0, numElements):
    if i%8 == 0 : print
    print randoms[i],

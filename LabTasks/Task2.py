from random import randint

__author__ = 'Vladislav'

# Number of dimensions of random matrix
NUM_ROWS = 4
NUM_COLS = 4

# Maximum number that can be randomly chosen.
MAX_NUMBER = 9


# Generating two dimensional array of random numbers
random_matrix = [[randint(0, MAX_NUMBER) for y in range(0, NUM_ROWS)] for x in range(0, NUM_COLS)]

# This list will contain entry count corresponding to randomly chosen number.
# index of list = number to each it corresponds
statistic = [0 for i in range(0, MAX_NUMBER+1)]

# Counting entries.
for y in range(0, NUM_ROWS):
    for x in range(0, NUM_COLS):
        element = random_matrix[x][y]
        statistic[element] += 1
    print

# Displaying how many times each element occurred.
for i in range(0, len(statistic)):
    print "Element " + str(i) + ": ",
    # printing '*" statistic[i] times.
    for j in range(0, statistic[i]):
        print '*',
    print # new line.



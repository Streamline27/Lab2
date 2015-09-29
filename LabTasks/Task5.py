__author__ = 'Vladislav'

NUM_ITERATIONS = 10

# This is example of recursive function.
def fibonacci(first, second, depth, num_iterations):
    # Termination
    if depth == num_iterations:
        return
    # Action
    print first,
    # Recursive call
    fibonacci(second, first+second, depth+1, num_iterations)


# Wrapper so it you don't have to assign all the variables correctly
def do_fibonacci(num_iterations):
    fibonacci(1, 1, 0, num_iterations)


do_fibonacci(NUM_ITERATIONS)
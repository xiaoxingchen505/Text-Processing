# Small program to demonstrate the relative efficiency of different approches to testing
# whether key is in a hash

from random import randint
import time

MAX_INT = 10000000
ITERATIONS = 100

# Create a large dictionary (with MAX_INT items)
dict = {}
for i in range(MAX_INT): 
    dict[i] = i


# Generate a random number and check whether its in the hash (it will be)
# Use APPROPRIATE approach to test
# Run this ITERATIONS times
t_start = time.time()
total_found = 0
for i in range(ITERATIONS): 
    rand = randint(0, MAX_INT)
    if rand in dict:
        total_found = total_found + 1
t_end = time.time()
t_diff = t_end - t_start
print("%d iterations took %.5f seconds" % (ITERATIONS, t_diff))

# Try again but this time use INAPPROPRIATE approach to check whether item in hash
t_start = time.time()
total_found = 0
for i in range(ITERATIONS): 
    rand = randint(0, MAX_INT)
    dict_keys = dict.keys()
    for k in dict_keys: 
        if k == rand: 
            total_found = total_found + 1
            break
t_end = time.time()
t_diff = t_end - t_start
print("%d iterations took %.5f seconds" % (ITERATIONS, t_diff))






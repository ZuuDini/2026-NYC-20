'''
for i in range(1, 20):
    print(i)
'''

from numpy import random

n = 5
random_numbers = random.randn(n)
print("Array of", n, "random numbers sampled from a standard normal distribution:")
print(random_numbers)

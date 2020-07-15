"""
This is a python programme that takes two integer lists of size N and returns their dot product.
Elements of the arrays are drawn as uniform variates between 1,1000
"""

# By Caleb Otchi
import random

# Initialising empty list variables. Values will be assigned in the function
list_a = []
list_b = []


def list_thing(N, ListA, ListB):

    # for loops to generate random integer values for both lists using N as the range
    for i in range(N):
        num = random.randint(1, 1000)
        ListA.append(num)

    for i in range(N):
        num = random.randint(1, 1000)
        ListB.append(num)

    # Prints out the values of both lists
    print("ListA =", ListA)
    print("ListB =", ListB)

    # Calculating the dot product of both lists abd storing in the variable (dot_product)
    dot_product = sum(x * y for x, y in zip(ListA, ListB))

    # This will print the dot product of both lists
    print("This is the dot product of both lists:", dot_product, "\n")


list_thing(10, list_a, list_b)
list_thing(100, list_a, list_b)
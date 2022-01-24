import random

def dice():
    square = [1, 2, 3, 4, 5, 6]
    numbers = random.choice(square)
    return numbers


print(dice())

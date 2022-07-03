import random


def subtraction_variants(a, b):
    y = random.randint(a, b)
    x = random.randint(a, b)
    task = str(y) + '-' + str(x)
    if y < x:
        task = str(x) + '-' + str(y)
    return task

print(subtraction_variants(1, 21))
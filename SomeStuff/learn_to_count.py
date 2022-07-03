import random
a = 1
b = 2

def division_variants(a, b):
    tsk_4_dvsn = []
    numbers = []

    for i in range(a, b):
        numbers.append(i)
    numbers = numbers[b - 1::-1]

    for j in numbers:
        for k in numbers:
            if j % k == 0:
                tsk_4_dvsn.append((j, k))
    task = random.choice(tsk_4_dvsn)
    y, x = task
    any_task = str(y) + '/' + str(x)
    return any_task


def subtraction_variants(a, b):
    y = random.randint(a, b)
    x = random.randint(a, b)
    task = str(y) + '-' + str(x)
    if y < x:
        task = str(x) + '-' + str(y)
    return task


def add_multi_cation(a, b):
    y = random.randint(a, b)
    x = random.randint(a, b)
    sign = ['+', '*']
    run_sing = random.choice(sign)
    task = str(y) + run_sing + str(x)
    return task

task = [division_variants(a, b), subtraction_variants(a, b), add_multi_cation(a, b)]


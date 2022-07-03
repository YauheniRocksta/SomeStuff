import random


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

print(division_variants(1, 21))
import random

x = random.randint(1, 20)
y = random.randint(1, 20)
# TODO замутить алгоритм для примера на деление, который будет отбирать из числового промежутка варианты деления
#  с целым остатком
variants = [(x + y), (x - y), (x / y), (x * y)]
task = random.choice(variants)

if task == variants[0]:
    print(1)
elif task == variants[1]:
    print(2)
    print('x = ' + str(x))
    print('y = ' + str(y))
    print('result = ' + str(task))
    if y > x:

        print('x = ' + str(x))
        print('y = ' + str(y))
        print('result = ' + str(y - x))
elif task == variants[2]:
    print(3)
elif task == variants[3]:
    print(4)


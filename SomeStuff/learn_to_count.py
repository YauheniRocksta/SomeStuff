import random

a = 1
b = 10


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
    return any_task, y / x


def subtraction_variants(a, b):
    y = random.randint(a, b)
    x = random.randint(a, b)
    task = str(y) + '-' + str(x)
    result = y - x
    if y < x:
        task = str(x) + '-' + str(y)
        result = x - y
    return task, result


def add_multi_cation(a, b):
    y = random.randint(a, b)
    x = random.randint(a, b)
    res_1 = y + x
    res_2 = y * x
    results = [res_1, res_2]
    run_res = random.choice(results)
    sing = ['+', '*']
    if run_res == res_1:
        sing = sing[0]
        result = res_1
    else:
        sing = sing[1]
        result = res_2
    task = str(y) + sing + str(x)
    return task, result


hp = 5
# Количество
score = 0
func_list = [subtraction_variants(a, b), division_variants(a, b), add_multi_cation(a, b)]
begin_text = 'Лалала три рубля!\nСча будит математика\n\nУ тебя есть Хэлсы' \
             '\nВот они\nНр х' + str(hp) + '\n\nИ есть очки\nГляди\nScore 0' + str(score) + '0' \
             '\n\nРешаешь матешу пральна - получаешь очки!\nНепральна - тратишь Хэлсы!' \
             'Набери максимальное количество очков ЙОПТА!\nКамон!'
print(begin_text)

while score < 999 and hp > 0:
    task = random.choice(func_list)
    print('\nРеши примерчик!\n')

    answer = input(task[0] + '= ')

    if int(answer) == task[1]:
        print('правильно')
        print('Hp x' + str(hp))
        score += 50
        if score < 100:
            print('Score 0' + str(score))
        else:
            print('Score ' + str(score))
    elif int(answer) != task[1]:
        print('ошибочка чел\nпопробуй ещё раз и не теряй хэлсы')
        hp -= 1
        print('Hp x' + str(hp))
        if score == 0:
            print('Score 0' + str(score) + '0')
        else:
            print('Score ' + str(score))
# TODO создать список с вариантами разных текстов для призыва решить пример!
# TODO написать код который будет давать бонусные очки если будет несколько правильных ответов подряд + фразы похвалы
#  за то что чел старается
# TODO фраза предупреждающая о последней жизни

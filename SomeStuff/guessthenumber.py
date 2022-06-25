import random
hp = 3
health = 'Количество попыток Х'
text_beg =('Угадайте число от 1 до 10!!!')
text_try_write = 'Введите число от 1 до 10!!!'
text_write = 'Введите ваше число: '
text_wrong = 'Неверное число!!'
text_win = 'Поздравляем! Вы угадали число!\nИгра завершена!'
text_done = 'Игра завершена! Попытки закончились'
text_more = 'Число больше заданного промежутка!'
text_less = 'Число меньше заданного промежутка'
text_try = 'Попробуйте снова!'
text_more_num = 'Ваше число больше загаданного.'
text_less_num = 'Ваше число меньше загаданного.'

print(text_beg)
# TODO найти варианты вывода данных в каждую строку
def main_game():
    hp = 3
    random_num = random.randint(1, 10)
    print(random_num)
    while hp >= 0:
        if hp == 0:
            print(text_done)
            break

        elif hp > 0:
            print(health + str(hp))
            player_num = int(input(text_write))

            if player_num == random_num:
                print(text_win)
                break
            elif player_num > random_num:
                print(text_wrong)
                hp -= 1
                if hp > 0:
                    print(text_more_num)
                    print(text_try)
            elif player_num < random_num:
                print(text_wrong)
                hp -= 1
                if hp > 0:
                    print(text_less_num)
                    print(text_try)

            elif player_num > 10:
                print(text_more)
                print(text_try_write)

            elif player_num < 0:
                print(text_less)
                print(text_try_write)


main_game()


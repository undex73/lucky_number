from random import *

def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= last_num:
        return True
    else:
        return False

def is_bound(num):
    if num.isdigit() and int(num) > 1:
        return True
    else:
        return False

def game():
    print('Добро пожаловать в мою игру - "Угадай число"')
    global last_num
    count = 0
    while count == 0:
        last_num = input('Введите верхнюю границу для числа: ')
        if not is_bound(last_num):
            print(f'Для старта игры нужно целое число больше 1')
        else:
            last_num = int(last_num)
            random_num = randint(1, last_num)
            count = 1
            print('Игра начинается')

    while True:
        user_num = input(f'Введите число для вашей {count} попытки: ')
        if not is_valid(user_num):
            print(f'Для начала игры нужно ввести целое число от 1 до {last_num}')
        else:
            user_num = int(user_num)
            if user_num == random_num:
                print(f'У вас получилось, число найдено! Вы угадали число с {count} попытки.')
                break
            elif user_num < random_num:
                print('Ваше число меньше загаданного, попробуйте еще раз')
                count += 1
            elif user_num > random_num:
                print('Ваше число больше загаданного, попробуйте еще раз')
                count += 1
    if input('Хотите сыграть ещё? да / нет ') == 'да':
        game()
    else:
        print('Спасибо за игру, буду рад видеть вас в следующий раз')

game()
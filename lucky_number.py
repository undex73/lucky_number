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
    print('Welcome to the game - "Lucky Number"')
    global last_num
    count = 0
    while count == 0:
        last_num = input('Enter upper bound for the number: ')
        if not is_bound(last_num):
            print(f'Need number more 1 to start the game.')
        else:
            last_num = int(last_num)
            random_num = randint(1, last_num)
            count = 1
            print('The game has started')

    while True:
        user_num = input(f'Enter number for your {count} try: ')
        if not is_valid(user_num):
            print(f'Better enter integer number from 1 to {last_num} to start the game')
        else:
            user_num = int(user_num)
            if user_num == random_num:
                print(f'You are lucky, number is found! You found number on {count} try.')
                break
            elif user_num < random_num:
                print('Your number is less than a "lucky" number, try again')
                count += 1
            elif user_num > random_num:
                print('Your number is more than a "lucky" number, try again')
                count += 1
    if input('Want to play again? yes or no ') == 'yes':
        game()
    else:
        print('Thanks for the game, welcome back any time')

game()
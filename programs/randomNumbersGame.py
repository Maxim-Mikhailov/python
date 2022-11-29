import random
guessesTaken = 0
print('Привет, как тебя зовут?')
myName = input()
number = random.randint(1, 20)
print('Что ж, ' + myName + ', Я ЗАГАДЫВАЮ ЧИСЛО ОТ 1 ДО 20.')
for guessesTaken in range(6):
    print('Попробуй угадать!')
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess ==number:
    guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + 'Ты справился(ась) за ' + guessesTaken + ' попытки!')

if guess !=number:
    number = str(number)
    print('Увы. Я загадала число ' + number + '.')


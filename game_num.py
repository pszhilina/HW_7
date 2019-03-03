import random
x = random.randint(0,10000)
i = 1
print('Компьютер загадал число.\n У вас есть три попытки. Удачи!')
while i<=3:
    try:
        num = int(input('Попробуйте угадать или введите "Выход": '))
        if num < x:
            print('Попробуйте число больше!')
        elif num > x:
            print ('Попробуйте число меньше!')
        else:
            print ('Победа!')
    except ValueError:
        print ('Вы вышли из игры.\n Число: ', x)
        break
    i += 1
else:
    print ('Game over!\n Число: ', x)

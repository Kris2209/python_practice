# Напишите программу, которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха |, а для горизонтальных — дефис -.
# Пусть пользователь вводит ширину и высоту рамки.


width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
for row in range(width):
    for col in range(height):
        if col == 0 or col == height-1:
            print('|', end='')
        elif row == 0 or row == width-1:
            print('-', end='')
        else:
            print(' ', end='')
    print()

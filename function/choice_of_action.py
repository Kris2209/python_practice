# Напишите программу, запрашивающую у пользователя число и действие, которое нужно с ним сделать: вывести сумму его цифр,
# максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

def master():
    x = int(input('Что необходимо сделать? 1 - вывести сумму цифр, 2 - найти максимальную цифру, 3 - найти минимальную цифру. '))
    if x == 1:
        summa_n()
    elif x == 2:
        max_n()
    elif x == 3:
        min_n()
    else:
        print('Ошибка ввода.')
        master()

def summa_n():
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
    number_3 = float(input('Введите третье число: '))
    summ = number_1 + number_2 + number_3
    print('Сумма чисел: ', summ)
    master()

def max_n():
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
    number_3 = float(input('Введите третье число: '))
    if number_3 < number_1 > number_2:
        print('Максимальное число:', number_1)
    elif number_3 < number_2 > number_1:
        print('Максимальное число:', number_2)
    else:
        print('Максимальное число:', number_3)
    master()

def min_n():
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
    number_3 = float(input('Введите третье число: '))
    if number_3 > number_1 < number_2:
        print('Минимальное число:', number_1)
    elif number_3 > number_2 < number_1:
        print('Минимальное число:', number_2)
    else:
        print('Минимальное число:', number_3)
    master()

master()
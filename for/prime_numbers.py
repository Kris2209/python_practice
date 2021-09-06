# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.


def is_prime(n):
    sqrt = n ** 0.5
    stop = int(sqrt + (sqrt % 1 > 0))

    for k in range(2, stop + 1):
        if (n % k == 0):
            return False

    return True

n = int(input('Сколько чисел будем проверять? '))
count = 0

for k in range(n):
    number = int( input(f'Введите { k + 1 } -е число: ') )
    if (is_prime(number)): count += 1

print()
print('В вашей последовательности ', count, ' простых чисел')
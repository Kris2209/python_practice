# Вводится N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
# Выведите на экран это число и сумму его цифр.



summ_1 = 0
max = 0
n = int(input('Введите количетство чисел: '))
for number in range(1, n+1):
    print('Введите', number, 'число: ', end='')
    numeral = int(input())
    while numeral > 0:
        number_1 = numeral % 10
        summ_1 += number_1
        numeral //= 10
    if max < summ_1:
        max = summ_1
    summ_1 = 0
    print(max)

print('Максимальная сумма цифр = ', max)
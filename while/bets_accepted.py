# Напишите программу, которая запрашивает у пользователя начальное количество денег и,
# пока оно меньше 10 000, запрашивает число, которое выпало на кубике (от 1 до 6).
# Если на кубике выпало 3, то выводится сообщение «Вы проиграли всё!», и деньги обнуляются.
# Если выпало другое число, к сумме прибавляется 500.


summ = int(input('Начальное количество денег: '))
while summ < 10000:
    cube = int(input('Какое число выпало на кубике? '))
    if cube == 3:
        print('Вы проиграли все!')
        summ = 0
        break
    summ += 500
    print('Вы выиграли 500 рублей!')
print('Игра закончена.')
print('Итого осталось: ', summ)
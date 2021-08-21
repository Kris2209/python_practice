# Георгий работает неофициально по часам, и его зарплата высчитывается по следующей формуле:
# http://joxi.ru/ZrJRlM1TbRE9br (ссылка на скриншот формулы).
# Он хочет понять, сколько часов нужно отработать, чтобы хватило на погашение кредита и еду.
# Напишите программу, которая запрашивает у пользователя три числа: количество отработанных часов,
# остаток по кредиту и количество денег на еду. После этого рассчитывается зарплата по формуле,
# и если зарплата больше либо равна денежной сумме, которая требуется на кредит и еду,
# то выводится сообщение: «Часов хватает. Можно отдохнуть», в противном случае: «Часов не хватает. Придётся работать!».


hours = int(input('Введите отработанные часы: '))
spending_on_food = int(input('Введите траты на еду: '))
credit = int(input('Введите остаток по кредиту: '))
remuneration = ((200 * hours)/2**3) + hours
if remuneration >= credit:
    print('Часов хватает. Можно отдохнуть!')
else:
    print('Часов не хватает. Придется работать!')
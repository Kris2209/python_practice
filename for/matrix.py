# Напишите программу, которая выводит на экран такую таблицу.
# http://joxi.ru/BA0JPo7Cv951Xm (ссылка на таблицу).

for row in range(0, 10):
    for col in range(0, -10, -1):
        print(col + row, end = '\t')
    print()


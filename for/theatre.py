# Планируется построить театр под открытым небом, но для начала нужно хотя бы примерно
# понять сколько должно быть рядов, сидений в них и какое лучше сделать расстояние между рядами.
# Напишите программу, которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# затем выводит примерный макет театра на экран.


row = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений в ряде: '))
meter = int(input('Введите кол-во метров между рядами: '))
print('Сцена')
for scene in range(row):
    print('=' * seat, end = ' ')
    print('*' * meter, end = ' ')
    print('=' * seat)

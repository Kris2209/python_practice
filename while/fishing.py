# Наши прекрасные родственники удачно сходили на рыбалку.
# Настолько, что ходили мешком перетаскивать рыбу с берега в машину целых n раз.
# Каждый мешок они взвешивали на электронных весах (все мешки весили по-разному).
# Напишите программу для весов, которая считает суммарный вес мешков и выводит его на экран.


bags = int(input('Сколько всего мешков? '))
total = 0
bags_count = 0
while bags != bags_count:
    weight = int(input('Сколько весит мешок? '))
    total += weight
    bags_count += 1
    print('Перенесено мешков', bags_count, 'из', bags)
print('Вес всего: ', total)
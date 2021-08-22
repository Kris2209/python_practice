# Напишите программу для немного усложнённой версии задачи про выигрышные билеты.
# Есть заранее известные номера билетов: 345, 19, 87, 1020 и 421 (можете брать свои номера, не стесняйтесь).
# Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на 5.
# Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.


i = 0
for ticket in 345, 19, 87, 1020, 421, 555:
    if ticket % 5 == 0 and ticket > 99 and ticket < 1000:
        i += 1
        print(ticket, 'Выиграшный билет!')
print('Количество счасливых билетов: ', i)
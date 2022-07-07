
names = []
texts = []
days = []
months = []
usernames = []

print('Закончить (при выборе действия) - enter')

while True:
    print(*names)
    print('Удалить участника - delete')
    print('Добавить участника - add')
    command = str(input())
    print()

    if command == 'delete':
        for index in range(len(names)):
            number = index + 1
            print(f'{number}. {names[index]}')
        choice = int(input('Введите номер человека, '
                           'которого вы хотите удалить: '))  - 1
        names.remove(names[choice])
        texts.remove(texts[choice])
        days.remove(days[choice])
        months.remove(months[choice])
        usernames.remove(usernames[choice])
        print()

    if command == 'add':
        name = str(input('Введите имя: '))
        names.append(name)
        text = str(input('Введите текст поздравления: '))
        texts.append(text)
        day = int(input('Введите день: '))
        days.append(day)
        month = int(input('Введите месяц (цифрой): '))
        months.append(month)
        username = str(input('Введите имя пользователя: '))
        usernames.append(username)
        print()
    if command == '':
        break

    if command != 'add' and command != 'delete' and command != '':
        print('Команда не распознана')
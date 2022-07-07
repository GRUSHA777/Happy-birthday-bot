
names = []
texts = []
days = []
months = []
usernames = []

print('End (when you choose an action) - enter')

while True:
    print(*names)
    print('Delete from the members list  - delete')
    print('Add member - add')
    command = str(input())
    print()

    if command == 'delete':
        for index in range(len(names)):
            number = index + 1
            print(f'{number}. {names[index]}')
        choice = int(input('Type in the number of person, you want'
                           'to delete: '))  - 1
        names.remove(names[choice])
        texts.remove(texts[choice])
        days.remove(days[choice])
        months.remove(months[choice])
        usernames.remove(usernames[choice])
        print()

    if command == 'add':
        name = str(input('Name: '))
        names.append(name)
        text = str(input('Text: '))
        texts.append(text)
        day = int(input('Day: '))
        days.append(day)
        month = int(input('Month (with a number): '))
        months.append(month)
        username = str(input('Telegram username: '))
        usernames.append(username)
        print()
    if command == '':
        break

    if command != 'add' and command != 'delete' and command != '':
        print('There is no such a command!')
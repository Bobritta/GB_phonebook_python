from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = address_data()
    with open('phonebook.csv', 'a', encoding='utf-8') as f:
        f.write(f'\n{name}; {surname}; {phone}; {adress};')
    

def print_data():
    print('На данный момент актуальна следующая версия справочника: \n')
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        lines_list = f.readlines()
        print(*lines_list)

def delete_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        print('\n На данный момент актуальна следующая версия справочника: \n')
        lines_list = f.readlines()
        for index, line in enumerate(lines_list, start=1):
            print(f"{index}: {line.strip()}")
        print('\n Какую запись Вы желаете удалить? Введите номер: \n')
        number = int(input())
    while number not in range(len(lines_list)+1):
        print("Вы ввели некорректное значение, попробуйте еще раз")
        number = int(input('Введите число: '))
    print(f'Вы хотите удалить запись {lines_list[number-1]}для подтверждения введите 1, для отмены - 2 \n')
    answer = int(input())
    while answer not in range (1, 3):
        print("Вы ввели некорректное значение, попробуйте еще раз")
        answer = int(input(f'Выберите (1) удаление записи {lines_list[number-1]} или (2) отмена: '))
    if answer == 1:
        with open('phonebook.csv', 'r', encoding='utf-8') as f:
            print(f'Запись {lines_list[number - 1]} удалена')
        del lines_list[number - 1]
        with open('phonebook.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines_list)
    elif answer == 2:
        print('Запись оставлена без изменений')

def correct_data():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        print('\n На данный момент актуальна следующая версия справочника: \n')
        lines_list = f.readlines()
        for index, line in enumerate(lines_list, start=1):
            print(f"{index}: {line.strip()}")
        print('\n Какую запись Вы желаете изменить? Введите номер: \n')
        number = int(input())
    while number not in range(1, len(lines_list)+1):
        print("Вы ввели некорректное значение, попробуйте еще раз")
        number = int(input('Введите число: '))
    print(f'Вы хотите изменить запись {lines_list[number-1]}для подтверждения введите 1, для отмены - 2 \n')
    answer = int(input())
    while answer not in range (1, 3):
        print("Вы ввели некорректное значение, попробуйте еще раз")
        answer = int(input(f'Выберите (1) изменение записи {lines_list[number-1]} или (2) отмена: '))
    if answer == 1:
        print(f'Вы выбрали изменение записи {lines_list[number-1]}. Введите новую версию записи: ')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        adress = address_data()
        if number == len(lines_list):
            new_data = f'{name}; {surname}; {phone}; {adress};'
        else:
            new_data = f'{name}; {surname}; {phone}; {adress};\n'
        lines_list[number-1] = new_data
        with open('phonebook.csv', 'w', encoding='utf-8') as f:
            f.writelines(lines_list)
        print('Запись успешно изменена.')
    else:
        print('Изменение отменено.')

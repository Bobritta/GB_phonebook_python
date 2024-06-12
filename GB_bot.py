from logger import input_data, print_data, delete_data

def interface():
    print("Добрый день! Вы попали на бот для работы с телефонным справочником! \n 1 - запись данных \n 2 - вывод данных \n 3 - редактирование записи \n 4 - удаление записи")
    command = int(input('Введите число: '))

    while command not in range(1, 5):
        print("Вы ввели некорректное значение, попробуйте еще раз")
        command = int(input('Введите число: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        print('В настоящее время функция не доступна, приносим свои извинения')
    elif command == 4:
        delete_data()

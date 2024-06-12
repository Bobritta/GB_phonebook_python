from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = address_data()
    with open('phonebook.csv', 'a', encoding='utf-8') as f:
        f.write(f'{name}; {surname}; {phone}; {adress};\n\n')
    

def print_data():
    print('На данный момент актуальна следующая версия справочника: \n')
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        lines_list = f.readlines()
        print(*lines_list)

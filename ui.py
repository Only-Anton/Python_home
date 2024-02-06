from logger import input_data, print_data
from home import delete_data, change_data

def interface():
    print("Добрый день! Вы в справочнике! \n 1 - записать данные \n 2 - вывести данные \n" 
        f" 3 - удалить данные \n 4 - исправить данные")
    command = int(input('Введите число: '))
    
    while command != 1 and command !=2 and command !=3 and command !=4:
        print('Неправильный ввод!')
        command =  int(input('Введите число [1, 2, 3, 4]: '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        change_data()
    
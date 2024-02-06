from data_create import name_data, surname_data, phone_data, address_data

def delete_data():
    choice = int(input("Выберите список в котором вы хотите произвести изменения (1 или 2):"))
    while choice != 1 and choice != 2:
        choice = int(input("У вас нет такого списка!!! Введите либо 1, либо 2:"))
    if choice == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            clear = input("Введите имя удаляемого контакта: ") + "\n"
            stop = 0
            for i in range(len(data_first)):
                if clear == data_first[i]:
                    stop = 1
                    n = i
            if stop == 0:
                print("Контакта с таким именем не существует! Учите свои записи!!!!")
            else:
                print("Вы действительно хотите удалить этот контакт:")
                for i in range(n, n+4):
                    print(data_first[i])
                anser = input("Да/Нет? ").lower()
                while anser != "да" and anser != "нет":
                    anser = input("Ну как так-то? вариантов-то ответа немного! \nДа/Нет? ").lower()
                if anser == "да":
                    data_first = data_first[0:n] + data_first[n+5:]
                    print("Запись успешно удалена! Вы - молодец!!!")
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in data_first:
                f.write(str(i))
    if choice == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            clear = input("Введите имя удаляемого контакта: ")
            l = len(clear)
            n = 0
            stop = 0
            for i in data_second:
                if clear == i[:l]:
                    stop = 1
                    numb = n
                n +=1
            if stop == 0:
                print("Учите свои записи!!! Такого контакта у вас нет!")
            else:
                print (f"Вы действительно хотите удалить этот контакт? \n{data_second[numb]}")
                anser = input("Да/Нет? ").lower()
                while anser != "да" and anser != "нет":
                    anser = input("Ну как так-то? вариантов-то ответа немного! \nДа/Нет? ").lower()
                if anser == "да":
                    data_second = data_second[:numb-1] + data_second[numb+1:]
                    print("Запись успешно удалена! Вы - молодец!!!")
                #print(*data_second)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in data_second:
                f.write(str(i))
                
def change_data():
    choice = int(input("Выберите список в котором вы хотите произвести изменения (1 или 2):"))
    while choice != 1 and choice != 2:
        choice = int(input("У вас нет такого списка!!! Введите либо 1, либо 2:"))
    if choice == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            clear = input("Введите имя контакта, который хотели бы изменить: ") + "\n"
            stop = 0
            for i in range(len(data_first)):
                if clear == data_first[i]:
                    stop = 1
                    n = i
            if stop == 0:
                print("Контакта с таким именем не существует! \nЕсть следующие контакты:")
                print(data_first)
            else:
                print("Вы действительно хотите изменгить этот контакт:")
                for i in range(n, n+4):
                    print(data_first[i])
                anser = input("Да/Нет? ").lower()
                while anser != "да" and anser != "нет":
                    anser = input("Ну как так-то? вариантов-то ответа немного! \nДа/Нет? ").lower()
                if anser == "да":
                    name = name_data()
                    surname = surname_data()
                    phone = phone_data()
                    address = address_data()
                    
                    modific = [f"{name}\n{surname}\n{phone}\n{address}\n\n"]
                    
                    data_first = data_first[0:n] + modific + data_first[n+5:]
                    print("Запись успешно изменена! Вы - молодец!!!")
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in data_first:
                f.write(str(i))
    if choice == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            clear = input("Введите имя контакта, который хотите изменить: ")
            l = len(clear)
            n = 0
            stop = 0
            for i in data_second:
                if clear == i[:l]:
                    stop = 1
                    numb = n
                n +=1
            if stop == 0:
                print("Учите свои записи!!! Такого контакта у вас нет!")
            else:
                print (f"Вы действительно хотите изменить этот контакт? \n{data_second[numb]}")
                anser = input("Да/Нет? ").lower()
                while anser != "да" and anser != "нет":
                    anser = input("Ну как так-то? вариантов-то ответа немного! \nДа/Нет? ").lower()
                if anser == "да":
                    name = name_data()
                    surname = surname_data()
                    phone = phone_data()
                    address = address_data()
        
                    modific = [f"{name};{surname};{phone};{address}\n"]
                    data_second = data_second[:numb] + modific + data_second[numb+1:]
                    print("Запись успешно изменена! Вы - молодец!!!")
                #print(*data_second)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in data_second:
                f.write(str(i))
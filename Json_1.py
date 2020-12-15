import json
import datetime
s = input('Если хотите добавить клиента - нажмите 1, если удалить - 2, если внести изменения - 3. Сделайте выбор: ')
if s !='1' and s !='2' and s !='3':
    print('Выберите 1, 2 или 3!')
if s == '1':
    repeat = ''
    new_client = {}
    while repeat == '':
        with open('data_file1.json', 'r', encoding='utf-8') as file:
            info = json.loads(file.read())
        count_id = info[-1].get('id') + 1
        new_client.update({'id': count_id})
        name = input('Введите имя: ')
        new_client.update({'name': name})
        last_name = input('Введите фамилию: ')
        new_client.update({'last_name': last_name})
        salary = input('Введите з/п: ')
        new_client.update({'salary': salary})
        age = input('Введите возраст: ')
        new_client.update({'age': age})
        position = input('Введите должность: ')
        new_client.update({'position': position})
        info.append(new_client)
        j = json.dumps(info, indent=4, ensure_ascii=False)
        with open('data_file1.json', 'w', encoding='utf-8') as file:
            file.write(j)
        with open('log_file1.txt', 'a', encoding='utf-8') as file:
            time = datetime.datetime.today()
            file.write(f'Запись {count_id} создана {time}\n')
        repeat = input('ENTER - продолжить работу со списком, любая другая клавиша + Enter - завершить')
elif s == '2':
    with open('data_file1.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    flag = ''
    while flag == '':
        try:
            d = int(input('Введите id клиента для удаления: '))
        except ValueError:
            print('Нужно ввести число!')
            continue
        for i in range(len(info)):
            if info[i].get('id') == d:
                info.pop(i)
                break
        flag = input('Чтобы продолжить удаление, нажмите ВВОД, для завершения любую клавишу')
    j = json.dumps(info, indent=4, ensure_ascii=False)
    with open('data_file1.json', 'w', encoding='utf-8') as file:
        file.write(j)
    with open('log_file1.txt', 'a', encoding='utf-8') as file:
        time = datetime.datetime.today()
        file.write(f'Запись {d} удалена {time}\n')
elif s == '3':
    with open('data_file1.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    d = int(input('Введите id клиента для изменений: '))
    for i in range(len(info)):
        if info[i].get('id') == d:
            print(info[i])
            s=''
            while s == '':
                change = input('Введите строку, в которую хотите внести изменения (name, last_name, salary, age, position): ')
                if change == "name":
                    old_name = info[i].get('name')
                    name = input('Введите новое имя: ')
                    info[i].update({'name': name})
                    with open('log_file1.txt', 'a', encoding='utf-8') as file:
                        time = datetime.datetime.today()
                        file.write(f'В записи {d} имя было изменено с {old_name} на {name} {time}\n')
                elif change == 'last_name':
                    old_last_name = info[i].get('last_name')
                    last_name = input('Введите новую фамилию: ')
                    info[i].update({'last_name': last_name})
                    with open('log_file1.txt', 'a', encoding='utf-8') as file:
                        time = datetime.datetime.today()
                        file.write(f'Фамилия была изменена с {old_last_name} на {last_name} {time}\n')
                elif change == 'salary':
                    old_salary = info[i].get('salary')
                    salary = input('Введите новую з/п: ')
                    info[i].update({'salary': salary})
                    with open('log_file1.txt', 'a', encoding='utf-8') as file:
                        time = datetime.datetime.today()
                        file.write(f'З/п была изменена с {old_salary} на {salary} {time}\n')
                elif change == 'age':
                    old_age = info[i].get('age')
                    age = input('Введите новый возраст: ')
                    info[i].update({'age': age})
                    with open('log_file1.txt', 'a', encoding='utf-8') as file:
                        time = datetime.datetime.today()
                        file.write(f'Возраст был изменен с {old_age} на {age} {time}\n')
                elif change == 'position':
                    old_position = info[i].get('position')
                    position = input('Введите новую должность: ')
                    info[i].update({'position': position})
                    with open('log_file1.txt', 'a', encoding='utf-8') as file:
                        time = datetime.datetime.today()
                        file.write(f'Должность была изменена с {old_position} на {position} {time}\n')
                else:
                    print('Введите верное поле для изменения')
                j = json.dumps(info, indent=4, ensure_ascii=False)
                with open('data_file1.json', 'w', encoding='utf-8') as file:
                    file.write(j)
                s = input('Чтобы продолжить изменения, нажмите ВВОД, для завержения любую клавишу')








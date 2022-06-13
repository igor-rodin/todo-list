# Отображение данных. взаимодействие с человеком
import time
from log import add2log


def add():  # Добавление данных
    print('Добавление записи')
    title = input('Введтие заголовок задачи: ')
    note = input('Описание задачи: ')
    status = input('Статус задачи: ')
    datetime = time.strftime("%Y.%m.%d %H:%M:%S", time.gmtime(time.time()))
    print('Данные добавлены')
    add2log(
        f'Добавление данных, Title = {title}, Note = {note}, Status = {status}')
    return {
        'title': title,
        'note': note,
        'status': status,
        'datetime': datetime
    }


def show_records(local_list):  # Отображение всей базы на экране красиво
    print(f'{"-"*1}Номер{"-"*1}+{"-"*25}Заголовок{"-"*25}+{"-"*3}Статус{"-"*3}+{"-"*7}Время{"-"*7}')
    for i in range(len(local_list)):
        print(
            f'{i:7}|{local_list[i]["title"]:59}|{local_list[i]["status"]:12}|{local_list[i]["datetime"]:11}')
    print(f'{"-"*7}+{"-"*59}+{"-"*12}+{"-"*19}')
    add2log(f'Выведено {len(local_list)} строк базы данных')


def del_records():  # Возвратим индекс элемента списка для удаления
    print('Введите номер записи, которую хотите удалить, или -1 - чтобы отказаться')
    ret = int(input('Номер записи: '))
    add2log(f'Удалена запись {ret}')
    return ret


def get_edit_records():  # Возвращаем индекс элемент списка для редактирования
    print('Введите номер записи, которую хотите редактировать, или -1 - чтобы отказаться')
    ret = int(input('Номер записи: '))
    return ret


def edit_record(local_list):  # Интерфейс редактирования записи
    print(f'Заголовок задачи: {local_list["title"]}')
    print(f'Описание задачи: {local_list["note"]}')
    print(f'Статус задачи: {local_list["status"]}')
    print('Введите новое значение, или оставьте поле пустым (Нажмите Enter)')
    title = ''
    note = ''
    status = ''
    inp = input('Введтие заголовок задачи: ')
    if len(inp) > 0:
        title = inp
    else:
        title = local_list["title"]
    inp = input('Описание задачи: ')
    if len(inp) > 0:
        note = inp
    else:
        note = local_list["note"]
    inp = input('Статус задачи: ')
    if len(inp) > 0:
        status = inp
    else:
        status = local_list["status"]
    datetime = time.strftime("%Y.%m.%d %H:%M:%S", time.gmtime(time.time()))
    add2log(
        f'Редактирование записи title {local_list["title"]} => {title}, {local_list["note"]} => {note},{local_list["status"]} => {status}')
    return {
        'title': title,
        'note': note,
        'status': status,
        'datetime': datetime
    }

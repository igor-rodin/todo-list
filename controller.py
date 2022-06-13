# Основная логика программы

from log import add2log
import view_module
import io_module

task_list = []

def init(): # Приветствие, и загрузка данных
    print('Ведение личных дел')
    print('/help - вывод помощи')
    return io_module.load_db()


def _help():
    print('Обрабатываются следующие команды:')
    print('\t /help - вывод помощи')
    print('\t /info - вывод информации о программе')
    print('\t /exit или /quit - выход из программы')
    print('\t /list - вывод списка дел')
    print('\t /add  - добавить новое дело')
    print('\t /edit - редактировать дело')
    print('\t /del  - удалить дело')
    print('\t /save - принудительно сохранить базу в файл')
    

def _info():
    print('Программа для ведения личных дел.')
    print('Выполнена в качестве командного домашнего задания')
    print('Коллективом из 4-х человек')

def _save(tasks): # Сохраняем в файл всю базу
    io_module.save_db(tasks)

def _list(tasks): # Выводим на экран всю базу
    view_module.show_records(tasks)

def _del(): # Возвращаем номер записи к удалению
    return view_module.del_records()

def _get_edit_idx(): # Возвращаем номер записи к редактированию
    return view_module.get_edit_records()

def controller(): # Главный цикл

    task_list = init() # Считываем всю базу из файла

    while True: 
        inp = input('>>> ')
        add2log(inp,'>') # Записываем в журнал все, что вводят
        match inp.lower():
            case '/help': _help()
            case '/info': _info()
            case '/exit': break
            case '/quit': break
            case '/list': _list(task_list)
            case '/add' : task_list.append(view_module.add())
            case '/edit':
                edit_idx = _get_edit_idx()
                if edit_idx > -1: 
                    save = task_list[edit_idx]
                    del task_list[edit_idx]
                    task_list.append(view_module.edit_record(save))

            case '/del' : 
                del_idx = _del()
                if del_idx > -1: del task_list[del_idx]    
            case '/save': 
                _save(task_list)
                print('Данные записаны на диск')
            case _ :
                print('Неверная команда. Для помощи наберите /help')
    _save(task_list)
    print('Выход из программы.')


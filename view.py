# Основная логика программы

from log import add2log
import controller
import io_module

task_list = []


def init():  # Приветствие, и загрузка данных
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


def _save(tasks):  # Сохраняем в файл всю базу
    io_module.save_db(tasks)


def _list(tasks):  # Выводим на экран всю базу
    controller.show_records(tasks)


def _del():  # Возвращаем номер записи к удалению
    return controller.del_records()


def _get_edit_idx():  # Возвращаем номер записи к редактированию
    return controller.get_edit_records()


def run_app():  # Главный цикл

    task_list = init()  # Считываем всю базу из файла

    while True:
        inp = input('>>> ')
        if inp.lower() == "/help":
            _help()
        elif inp.lower() == "/info":
            _info()
        elif inp.lower() == "/exit" or inp.lower() == "/quit":
            _save(task_list)
            print('Выход из программы.')
            break
        elif inp.lower() == "/list":
            _list(task_list)
        elif inp.lower() == "/add":
            task_list.append(controller.add())
        elif inp.lower() == "/edit":
            edit_idx = _get_edit_idx()
            if edit_idx > -1:
                save = task_list[edit_idx]
                del task_list[edit_idx]
                task_list.append(controller.edit_record(save))
        elif inp.lower() == "/del":
            del_idx = _del()
            if del_idx > -1:
                del task_list[del_idx]
        elif inp.lower() == "/save":
            _save(task_list)
            print('Данные записаны на диск')
        else:
            print('Неверная команда. Для помощи наберите /help')


import model.todo_item as tdi

todo_list = []


def init(td_list):
    global todo_list
    todo_list = td_list


def add_item(item: tdi.todo_item):
    todo_list.append(item)


def get_item(id: int) -> tdi.todo_item:
    return tdi.create_item(todo_list[id].title, todo_list[id].date, todo_list[id].is_done)


def del_item(id: int):
    todo_list.pop(id)


def change_title(id: int, new_val: str):
    old_item = todo_list.pop(id)
    todo_list.insert(id, tdi.create_item(
        new_val, old_item.date, old_item.is_done))


def change_done(id: int):
    old_item = todo_list.pop(id)
    todo_list.insert(id, tdi.create_item(
        old_item.title, old_item.date, not old_item.is_done))


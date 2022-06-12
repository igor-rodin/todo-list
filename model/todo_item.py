from collections import namedtuple as nt
from datetime import datetime

todo_item = nt("ToDoItem", "title date is_done")

def create_item(title: str, date = datetime.now().strftime("%d.%m.%Y [%H:%M]"), is_done = False)-> todo_item:
    return todo_item(title, date, is_done)

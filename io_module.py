# Процедуры работы с базой данных

import settings
import json
import os

def load_db(): # читаем из файла json в список словарей
    if os.path.isfile(settings.db_file):
        with open(settings.db_file, 'r', encoding='UTF-8') as f:
            ret = json.load(f)
            return ret
    else: return []

def save_db(local_list): # пишем в файл json список словарей
    if len(local_list) > 0:
        with open(settings.db_file, 'w', encoding='UTF-8') as f:
            json.dump(local_list, f)
    return

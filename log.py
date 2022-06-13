# Функционал работы с журналом

import time
import settings


def add2log(text):  # записываем всё в файл-лог
    with open(settings.LOG_FILE, 'a', encoding='UTF-8') as f:
        f.write(
            f'{time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))},{text}\n')

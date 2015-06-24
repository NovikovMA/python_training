# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


from model.group import Group                                               # Модель группы контактов адресной книги
import getopt                                                               # Чтение опций командной строки
import jsonpickle                                                           # Работа с файлами формата JSON
import os.path                                                              # Работа с файлами и путями к ним
import random                                                               # Случайности
import string                                                               # Строки
import sys                                                                  # Доступ к опциям командной строки


# Блок получения опций командной строки и их значений
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
# Значения по умолчанию
n = 5                                                                       # Количесвто пачек тестовых данных
f = "data/groups.json"                                                      # Файл для записи тестовых данных
# Разбор полученных значений
for o, a in opts:                                                           # Цикл по всем полученным опциям
    if o == "-n":                                                           # При нахождении "-n"
        n = int(a)                                                          # Определение количества пачек тестовых данных
    elif o == "-f":                                                         # При нахождении "-f"
        f = a                                                               # Определение имени файла для записи тестовых данных


# Получение случайной строки
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10    # Используемы символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # Строка


# Случайные тестовые данные
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)    # Определение пути к файлу для записи тестовых данных
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)                        # Установка формата вывода данных в файл
    out.write(jsonpickle.encode(testdata))                                  # Перевод тестовых данных в формат JSON

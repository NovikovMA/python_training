# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


from model.address import Address                                           # Модель контакта адресной книги
import datetime                                                             # Дата и время
import getopt                                                               # Чтение опций командной строки
import jsonpickle                                                           # Работа с файлами формата JSON
import os.path                                                              # Работа с файлами и путями к ним
import random                                                               # Случайности
import string                                                               # Строки
import sys                                                                  # Доступ к опциям командной строки


# Блок получения опций командной строки и их значений
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of addresses", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
# Значения по умолчанию
n = 2                                                                       # Количесвто пачек тестовых данных
f = "data/addresses.json"                                                   # Файл для записи тестовых данных
# Разбор полученных значений
for o, a in opts:                                                           # Цикл по всем полученным опциям
    if o == "-n":                                                           # При нахождении "-n"
        n = int(a)                                                          # Определение количества пачек тестовых данных
    elif o == "-f":                                                         # При нахождении "-f"
        f = a                                                               # Определение имени файла для записи тестовых данных


# Получение случайной строки
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10                 # Используемы символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # Строка


# Получение случайной строки со знаками пунктуации
def random_string_punctuation(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10    # Используемы символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # Строка


# Получение случайного текста
def random_text(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + "\n"*3        # Используемы символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # Текст


# Получение случайного текста со знаками пунктуации и дополнительными печатными символами
def random_text_printable(prefix, maxlen):
    symbols = string.printable + " "*10 + "\n"*3                            # Используемы символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # Текст


# Случайные тестовые данные
testdata = [Address(first_name="", middle_name="", last_name="", nickname="",
                    title="", company="", address="",
                    tel_home="", tel_mobile="", tel_work="", tel_fax="",
                    web_email="", web_email2="", web_email3="", web_homepage="",
                    birthday_day=0, birthday_month=0, birthday_year="",
                    anniversary_day=0, anniversary_month=0, anniversary_year="",
                    sec_address="", home="", notes="")] + [
    Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov",
            title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4",
            tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59",
            web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru",
            birthday_day=14, birthday_month=11, birthday_year="1986",
            anniversary_day=1, anniversary_month=1, anniversary_year="2000",
            sec_address="Secondary Address", home="Home", notes="Notes")] + [
    Address(first_name=random_string("", 20), middle_name=random_string("", 20), last_name=random_string("", 20), nickname=random_string("", 20),
            title=random_string("", 20), company=random_string("", 20), address=random_text("", 100),
            tel_home=random_string("", 20), tel_mobile=random_string("", 20), tel_work=random_string("", 20), tel_fax=random_string("", 20),
            web_email=random_string("", 20), web_email2=random_string("", 20), web_email3=random_string("", 20), web_homepage=random_string("", 20),
            birthday_day=random.randrange(1, 31), birthday_month=random.randrange(1, 12), birthday_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            anniversary_day=random.randrange(1, 31), anniversary_month=random.randrange(1, 12), anniversary_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            sec_address=random_text("", 100), home=random_string("", 20), notes=random_text("", 100))
    for i in range(n)] + [
    Address(first_name=random_string_punctuation("", 20), middle_name=random_string_punctuation("", 20), last_name=random_string_punctuation("", 20), nickname=random_string_punctuation("", 20),
            title=random_string_punctuation("", 20), company=random_string_punctuation("", 20), address=random_text_printable("", 100),
            tel_home=random_string_punctuation("", 20), tel_mobile=random_string_punctuation("", 20), tel_work=random_string_punctuation("", 20), tel_fax=random_string_punctuation("", 20),
            web_email=random_string_punctuation("", 20), web_email2=random_string_punctuation("", 20), web_email3=random_string_punctuation("", 20), web_homepage=random_string_punctuation("", 20),
            birthday_day=random.randrange(1, 31), birthday_month=random.randrange(1, 12), birthday_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            anniversary_day=random.randrange(1, 31), anniversary_month=random.randrange(1, 12), anniversary_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            sec_address=random_text_printable("", 100), home=random_string_punctuation("", 20), notes=random_text_printable("", 100))
    for j in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)    # Определение пути к файлу для записи тестовых данных
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)                        # Установка формата вывода данных в файл
    out.write(jsonpickle.encode(testdata))                                  # Перевод тестовых данных в формат JSON

# -*- coding: utf-8 -*-
from model.address import Address                                           # Модель контакта адресной книги
import datetime                                                             # Дата и время
import pytest                                                               # Среда исполнения
import random                                                               # Случайности
import string                                                               # Строки


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


# Набор данных для использования в тестовом сценарии
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
    for i in range(2)] + [
    Address(first_name=random_string_punctuation("", 20), middle_name=random_string_punctuation("", 20), last_name=random_string_punctuation("", 20), nickname=random_string_punctuation("", 20),
            title=random_string_punctuation("", 20), company=random_string_punctuation("", 20), address=random_text_printable("", 100),
            tel_home=random_string_punctuation("", 20), tel_mobile=random_string_punctuation("", 20), tel_work=random_string_punctuation("", 20), tel_fax=random_string_punctuation("", 20),
            web_email=random_string_punctuation("", 20), web_email2=random_string_punctuation("", 20), web_email3=random_string_punctuation("", 20), web_homepage=random_string_punctuation("", 20),
            birthday_day=random.randrange(1, 31), birthday_month=random.randrange(1, 12), birthday_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            anniversary_day=random.randrange(1, 31), anniversary_month=random.randrange(1, 12), anniversary_year=str(random.randrange(datetime.MINYEAR, datetime.MAXYEAR)),
            sec_address=random_text_printable("", 100), home=random_string_punctuation("", 20), notes=random_text_printable("", 100))
    for i in range(2)
]


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])  # Добавление возможности использование тестовых данных в сценарии, определение вывода результатов выполнения теста
def test_add_address(app, address):
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    app.address.create(address)                                             # Создание нового контакта
    assert len(old_addresses) + 1 == app.address.count()                    # Проверка соответсвия длин списков контактов до и после добавления элемента
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов


#def test_add_empty_address(app):
#    old_addresses = app.address.get_address_list()                          # Получение списка контактов
#    address = Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", tel_home="", tel_mobile="", tel_work="", tel_fax="", web_email="", web_email2="", web_email3="", web_homepage="", birthday_day=0, birthday_month=0, birthday_year="", anniversary_day=0, anniversary_month=0, anniversary_year="", sec_address="", home="", notes="")
#    app.address.create(address)                                             # Создание нового контакта
#    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
#    assert len(old_addresses) + 1 == len(new_addresses)                     # Проверка соответсвия длин списков контактов до и после добавления элемента
#    old_addresses.append(address)                                           # добавление элемента в старый список
#    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов

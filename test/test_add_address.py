# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    address = Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")
    app.address.create(address)                                             # Создание нового контакта
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    assert len(old_addresses) + 1 == len(new_addresses)                     # Проверка соответсвия длин списков контактов до и после добавления элемента
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов



def test_add_empty_address(app):
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    address = Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", tel_home="", tel_mobile="", tel_work="", tel_fax="", web_email="", web_email2="", web_email3="", web_homepage="", birthday_day=0, birthday_month=0, birthday_year="", anniversary_day=0, anniversary_month=0, anniversary_year="", sec_address="", home="", notes="")
    app.address.create(address)                                             # Создание нового контакта
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    assert len(old_addresses) + 1 == len(new_addresses)                     # Проверка соответсвия длин списков контактов до и после добавления элемента
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов

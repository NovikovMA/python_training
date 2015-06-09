# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
from random import randrange


def test_delete_address(app):                                               # Тест удаления контакта
    if app.address.count() == 0:                                            # Проверка наличия хотябы одного контакта в списке
        app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    index = randrange(len(old_addresses))                                   # Получение случайного порядкового номера
    app.address.delete_address_by_index(index)                              # Удаление контакта
    assert len(old_addresses) - 1 == app.address.count()                    # Проверка соответсвия длин списков контактов до и после удаление элемента
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    old_addresses[index:index+1] = []                                       # Удаление первого элемента списка
    assert old_addresses == new_addresses                                   # Сравнение списков контактов

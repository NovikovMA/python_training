# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
import random                                                               # Случайности


def test_delete_address(app, db, check_ui):                                 # Тест удаления контакта
    if len(db.get_address_list()) == 0:                                     # Проверка наличия хотябы одного контакта в списке
        app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
    old_addresses = db.get_address_list()                                   # Получение списка контактов
    address = random.choice(old_addresses)                                  # Выбор случайного контакта
    app.address.delete_address_by_id(address.id)                            # Удаление контакта
    new_addresses = db.get_address_list()                                   # Получение нового списка контактов
    assert len(old_addresses) - 1 == len(new_addresses)                     # Проверка соответсвия длин списков контактов до и после удаление элемента
    old_addresses.remove(address)                                           # Удаление первого элемента списка
    assert old_addresses == new_addresses                                   # Сравнение списков контактов
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)

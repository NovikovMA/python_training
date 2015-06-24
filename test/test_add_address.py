# -*- coding: utf-8 -*-
from model.address import Address                                           # Модель контакта адресной книги


# Использование тестовых данных из py-файла
def test_add_address_data(app, data_addresses):
    address = data_addresses
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    app.address.create(address)                                             # Создание нового контакта
    assert len(old_addresses) + 1 == app.address.count()                    # Проверка соответсвия длин списков контактов до и после добавления элемента
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов


# Использование тестовых данных из json-файла
def test_add_address_json(app, json_addresses):
    address = json_addresses
    old_addresses = app.address.get_address_list()                          # Получение списка контактов
    app.address.create(address)                                             # Создание нового контакта
    assert len(old_addresses) + 1 == app.address.count()                    # Проверка соответсвия длин списков контактов до и после добавления элемента
    new_addresses = app.address.get_address_list()                          # Получение нового списка контактов
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов

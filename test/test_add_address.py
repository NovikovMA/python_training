# -*- coding: utf-8 -*-
from model.address import Address                                           # Модель контакта адресной книги


# Использование тестовых данных из py-файла
def test_add_address_data(app, db, check_ui, data_addresses):
    address = data_addresses
    old_addresses = db.get_address_list()                                   # Получение списка контактов
    app.address.create(address)                                             # Создание нового контакта
    new_addresses = db.get_address_list()                                   # Получение нового списка контактов
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)


# Использование тестовых данных из json-файла
def test_add_address_json(app, db, check_ui, json_addresses):
    address = json_addresses
    old_addresses = db.get_address_list()                                   # Получение списка контактов
    app.address.create(address)                                             # Создание нового контакта
    new_addresses = db.get_address_list()                                   # Получение нового списка контактов
    old_addresses.append(address)                                           # добавление элемента в старый список
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)

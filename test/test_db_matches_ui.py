# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
from model.group import Group                                               # Модель группы контактов адресной книги
import re                                                                   # Регулярные выражения


# Тест сравнения списков групп, полученных из базы данных и через пользовательский интерфейс
def test_group_list(app, db):
    def clean(group):                                                       # Уделение пробелов в начале и конце наименований групп, перевод идентификаторов в стройчный формат
        return Group(id=str(group.id), name=group.name.strip())             # Модифицированная для сравнения группа
    db_list = list(map(clean, db.get_group_list()))                         # Список групп из базы данных, без начинающих и завершающих пробелов, приведенные к строковоку формату
    ui_list = app.group.get_group_list()                                    # Список групп с экрана
    assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)

# Тест сравнения списков контактов, полученных из базы данных и через пользовательский интерфейс
def test_address_list(app, db):
    def clean(address):                                                     # Уделение последовательностей пробелов, перевод идентификаторов в стройчный формат
        return Address(id=str(address.id), first_name=re.sub(r'\s{2,}', ' ', address.first_name).strip(), last_name=re.sub(r'\s{2,}', ' ', address.last_name).strip())  # Модифицированная для сравнения контактов
    db_list = list(map(clean, db.get_address_list()))                       # Список контактов из базы данных, без начинающих и завершающих пробелов, приведенные к строковоку формату
    ui_list = app.address.get_address_list()                                # Список контактов с экрана
    assert sorted(db_list, key=Address.id_or_max) == sorted(ui_list, key=Address.id_or_max)

# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from datetime import datetime
from pymysql.converters import decoders                                     # Преобразование данных
from model.address import Address                                           # Модель контакта адресной книги
from model.group import Group                                               # Модель группы контактов адресной книги
from pony.orm import *


class ORMFixture:

    db = Database()

    # Структура объектов, привязываемых к базе данных
    class ORMGroup(db.Entity):                                              # Группа
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        addresses = Set(lambda: ORMFixture.ORMAddress,
                        table="address_in_groups",
                        column="id", reverse="groups",
                        lazy=True)                                          # Связанные контакты (объект ORM, таблица базы, идентификатор связываемого параметра в базе, наименование связываемого параметра в ORM-объекте, с отключенной загрузкой при создании объекта)

    # Структура объектов, привязываемых к базе данных
    class ORMAddress(db.Entity):                                            # Контакт
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table="address_in_groups",
                     column="group_id",reverse="addresses",
                     lazy=True)                                             # Связанные группы

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password, conv=decoders)  # Подключение к базе данных с разрешением преобразования данных в извесные форматы
        self.db.generate_mapping()                                          # Сопоставление объектов класса и таблиц базы данных
        #sql_debug(True)                                                     # Вывод формируемых sql-запросов в консоль

    # Уничтожение фикстуры работы с базой данных
    def destroy(self):
        pass

    # Преобразование объектов ORMGroup (текущий формат) к формату объектов model (общий формат)
    def convert_groups_to_model(self, groups):
        def convert(group):                                                 # Преобразование одного объекта группы
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))                                   # Преобразованный список групп

    # Преобразование объектов ORMAddress (текущий формат) к формату объектов model (общий формат)
    def convert_addresses_to_model(self, addresses):
        def convert(address):                                               # Преобразование одного объекта группы
            return Address(id=str(address.id), first_name=address.firstname, last_name=address.lastname)
        return list(map(convert, addresses))                                   # Преобразованный список групп

    # Получение списка групп
    @db_session                                                             # Метка выполнения функции в рамках единой сессии
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup)) # Получение (запрос к базе) списка групп

    # Получение списка контактов
    @db_session                                                             # Метка выполнения функции в рамках единой сессии
    def get_address_list(self):
        return self.convert_addresses_to_model(select(a for a in ORMFixture.ORMAddress if a.deprecated is None)) # Получение (запрос к базе) списка контактов

    # Получение списка контактов, включенных в группу
    @db_session                                                             # Метка выполнения функции в рамках единой сессии
    def get_addresses_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0] # Получение группы из базы в формате ORM
        return self.convert_addresses_to_model(orm_group.addresses)         # Список контактов в понятном формате

    # Получение списка контактов, не включенных в группу
    @db_session                                                             # Метка выполнения функции в рамках единой сессии
    def get_addresses_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0] # Получение группы из базы в формате ORM
        return self.convert_addresses_to_model(
            select(a for a in ORMFixture.ORMAddress if a.deprecated is None and orm_group not in a.groups)) # Получение (запрос к базе) списка контактов

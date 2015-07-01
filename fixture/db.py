# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
from model.group import Group                                               # Модель группы контактов адресной книги
import mysql.connector                                                      # Работа с базами данных mysql


# Фикстуры работы с базой данных
class DbFixture():

    # Создание фикстуры работы с базой данных
    def __init__(self, host, name, user, password):
        self.host = host                                                    # Наименование хоста
        self.name = name                                                    # Имя базы данных
        self.user = user                                                    # Имя пользователя для подключения
        self.password = password                                            # Пароль пользователя для подключения
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)   # Подключение к базе данных
        self.connection.autocommit = True                                   # Отключение внутреннего кеширования управления базой данных

    # Получение списка контактов из базы данных
    def get_address_list(self):
        addresses = []                                                      # Список контактов пуст
        cursor = self.connection.cursor()                                   # Начать работу с элементами базы данных
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")   # Выполнение SQL-запроса в базе
            for row in cursor:                                              # Перебор полученной из базы данных структуры по строкам
                (id, first_name, last_name, address,
                 home_phone, mobile_phone, work_phone, secondary_phone,
                 web_email, web_email2, web_email3) = row                   # Разбиение строки на простые переменные
                addresses.append(Address(id=id, first_name=first_name, last_name=last_name,
                                         address=address,
                                         tel_home=home_phone, tel_mobile=mobile_phone, tel_work=work_phone, home=secondary_phone,
                                         web_email=web_email, web_email2=web_email2, web_email3=web_email3))    # Добавление контакта, полученного из базы данных, в список контактов
        finally:
            cursor.close()                                                  # Завершить работу с элементами базы данных
        return addresses                                                    # Список контактов

    # Получение списка групп из базы данных
    def get_group_list(self):
        groups = []                                                         # Список групп пуст
        cursor = self.connection.cursor()                                   # Начать работу с элементами базы данных
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")   # Выполнение SQL-запроса в базе
            for row in cursor:                                              # Перебор полученной из базы данных структуры по строкам
                (id, name, header, footer) = row                            # Разбиение строки на простые переменные
                groups.append(Group(id=id, name=name, header=header, footer=footer))    # Добавление группы, полученной из базы данных, в список групп
        finally:
            cursor.close()                                                  # Завершить работу с элементами базы данных
        return groups                                                       # Список групп

    # Уничтожение фикстуры работы с базой данных
    def destroy(self):
        self.connection.close()

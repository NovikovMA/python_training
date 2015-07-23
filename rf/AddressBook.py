# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from fixture.application import Application
from fixture.db import DbFixture                                            # Настройки работы с базой данных
from fixture.orm import ORMFixture                                          # Работа с базой данных через ORM-подсистему
from model.address import Address                                           # Модель контакта адресной книги
import json                                                                 # Работа с файлами формата JSON
import os.path                                                              # Работа с файлами и путями к ним


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'                                      # Едиый объект для всего тестового набора

    def __init__(self, config="target.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)    # Определение пути к конфигурационному файлу по умолчанию
        with open(config_file) as f:                                        # Открыть файл, контроль автоматического закрытия после выполнения блока команд
            self.target = json.load(f)                                      # Загрузка данных из файла

    # Инициализация (создание) фикстур
    def init_fixtures(self):
        web_config = self.target["web"]                                     # Получение данных конфигурации выполнения из файла для работы с Web
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password']) # Авторизация пользователя
        db_config = self.target['db']                                       # Получение данных конфигурации выполнения из файла для работы с базой данных
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])   # Создание фикстуры работы с базой данных
        orm_config = self.target['db']                                      # Получение данных конфигурации выполнения из файла для работы с базой данных
        self.ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'], password=orm_config['password'])   # Создание фикстуры работы с базой данных

    # Уничтожение фикстур
    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()
        self.ormfixture.destroy()

    # Определение контакта
    def new_address(self, first_name, middle_name, last_name, address):
        return Address(first_name=first_name, middle_name=middle_name, last_name=last_name, address=address)    # Контакт

    # Переопределение контакта по идетфикатору
    def new_address_with_id(self, id, first_name, middle_name, last_name, address):
        return Address(id=id, first_name=first_name, middle_name=middle_name, last_name=last_name, address=address)    # Контакт

    # Получение идентификатора контакта из списка по его номеру
    def get_address_id_by_index_from_the_list(self, index, address_list):
        return address_list[index].id                                       # Тдентификатор контакта

    # Получение списка контактов
    def get_address_list(self):
        return self.ormfixture.get_address_list()                           # Список контактов

    # Получение непустого списка контактов
    def get_not_empty_address_list(self):
        if len(self.ormfixture.get_address_list()) == 0:                    # Проверка наличия хотябы одного контакта в списке
            self.fixture.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes"))    # Создание контакта на случай пустого списка
        return self.get_address_list()                                      # Список контактов

    # Создание контакта
    def create_address(self, address):
        self.fixture.address.create(address)                                # Создание нового контакта

    # Удаление контакта
    def delete_address(self, address):
        self.fixture.address.delete_address_by_id(address.id)               # Удаление контакта по идентификатору

    # Изменение контакта
    def modify_address(self, address):
        self.fixture.address.modify_address_by_id(address)                  # Изменение контакта по идентификатору

    # Проверка равенства списков контактов
    def address_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Address.id_or_max) == sorted(list2, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов

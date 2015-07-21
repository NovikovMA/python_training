# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
from pytest_bdd import given, when, then                                    # Определение служебны слов BDD (метки)
from random import randrange                                                # Случайности
import pytest                                                               # Исполнение тестов
import random                                                               # Случайности


# Получение списка контактов
@pytest.allure.step('Given a address list')                                 # Метка присутсвия сообщения в отчете
@given('a address list')                                                    # Метка определения фразы тестового сценария
def address_list(db):
    return db.get_address_list()                                            # Получение списка контактов


# Определение нового контакта
@pytest.allure.step('Given a address with first_name={first_name}, middle_name={middle_name}, last_name={last_name} and address={address}')     # Метка присутсвия сообщения в отчете
@given('a address with <first_name>, <middle_name>, <last_name> and <address>') # Метка определения фразы тестового сценария
def new_address(first_name, middle_name, last_name, address):
    return Address(first_name=first_name, middle_name=middle_name, last_name=last_name, address=address)    # Новый контакт


# Добавление нового контакта
@when('I add address to the list')                                          # Метка определения фразы тестового сценария
def add_new_address(app, new_address):
    with pytest.allure.step('when I add address to the list'):
        app.address.create(new_address)                                     # Создание нового контакта


# Проверка успешного добавления контакта
@then('the new address list is equal to the old list with the added address')   # Метка определения фразы тестового сценария
def verify_address_added(app, db, check_ui, address_list, new_address):
    with pytest.allure.step('Then the new address list is equal to the old list with the added address'):
        old_addresses = address_list                                        # Получение списка контактов
        new_addresses = db.get_address_list()                               # Получение нового списка контактов
        old_addresses.append(new_address)                                   # Добавление элемента в старый список
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов
        if check_ui:                                                        # Проверка необходимости дополнительной проверки пользовательского интерфейса
            assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)


# Получение непустого списка контактов
@pytest.allure.step('Given a non-empty address list')                       # Метка присутсвия сообщения в отчете
@given('a non-empty address list')                                          # Метка определения фразы тестового сценария
def non_empty_address_list(app, db):
    if len(db.get_address_list()) == 0:                                     # Проверка наличия хотябы одного контакта в списке
        app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
    return db.get_address_list()                                            # Получение списка контактов


# Выбор случайного контакта из списка
@pytest.allure.step('Given a random address from the list')                 # Метка присутсвия сообщения в отчете
@given('a random address from the list')                                    # Метка определения фразы тестового сценария
def random_address(non_empty_address_list):
    return random.choice(non_empty_address_list)                            # Выбор случайного контакта


# Удаление контакта
@when('I delete the address from the list')                                 # Метка определения фразы тестового сценария
def delete_address(app, random_address):
    with pytest.allure.step('When I delete the address %s from the list' % random_address):
        app.address.delete_address_by_id(random_address.id)                 # Удаление контакта


# Проверка успешного удаления контакта
@then('the new address list is equal to the old list with the deleted address') # Метка определения фразы тестового сценария
def verify_address_deleted(app, db, check_ui, non_empty_address_list, random_address):
    with pytest.allure.step('Then the new address list is equal to the old list with the deleted address'):
        old_addresses = non_empty_address_list                              # Получение списка контактов
        new_addresses = db.get_address_list()                               # Получение нового списка контактов
        old_addresses.remove(random_address)                                # Удаление первого элемента списка
        assert old_addresses == new_addresses                               # Сравнение списков контактов
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        with pytest.allure.step('Also check UI'):
            assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)


# Выбор случайного контакта из списка для модификации
@pytest.allure.step('Given a random address from the list for modify')      # Метка присутсвия сообщения в отчете
@given('a random address from the list for modify')                         # Метка определения фразы тестового сценария
def random_address_index(non_empty_address_list):
    return randrange(len(non_empty_address_list))                           # Получение случайного порядкового номера


# Изменение контакта
@when('I modify the address from the list')                                 # Метка определения фразы тестового сценария
def modify_address(app, non_empty_address_list, random_address_index, new_address):
    with pytest.allure.step('When I modify the address from the list'):
        new_address.id = non_empty_address_list[random_address_index].id    # Установка идентификатора изменяемого элемента
        app.address.modify_address_by_id(new_address)                       # Изменение параметров контакта


# Проверка успешного удаления контакта
@then('the new address list is equal to the old list with the modified address')    # Метка определения фразы тестового сценария
def verify_address_modified(app, db, check_ui, non_empty_address_list, random_address_index, new_address):
    with pytest.allure.step('Then the new address list is equal to the old list with the modified address'):
        old_addresses = non_empty_address_list                              # Получение списка контактов
        new_addresses = db.get_address_list()                               # Получение нового списка контактов
        old_addresses[random_address_index] = new_address                   # Изменение контакта в старом списке
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max) # Сравнение сортированных по идентификатору списков контактов
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        with pytest.allure.step('Also check UI'):
            assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_group_list(), key=Address.id_or_max)

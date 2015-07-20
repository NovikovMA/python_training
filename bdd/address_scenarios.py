# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from pytest_bdd import scenario                                             # Запуск тестов BDD
from .address_steps import *                                                # Определение шагов тестов


@scenario('addresses.feature', 'Add new address')                           # Метка параметров исполнения тестового сценария
def test_add_new_address():                                                 # Тест добавления нового контакта
    pass


@scenario('addresses.feature', 'Delete a address')                          # Метка параметров исполнения тестового сценария
def test_delete_address():                                                  # Тест удаления случайного контакта
    pass


@scenario('addresses.feature', 'Modify a address')                          # Метка параметров исполнения тестового сценария
def test_modify_address():                                                  # # Тест изменения случайного контакта
    pass

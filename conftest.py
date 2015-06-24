# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

import importlib
import jsonpickle                                                           # Работа с файлами формата JSON
import json                                                                 # Работа с файлами формата JSON
import pytest
import os.path                                                              # Работа с файлами и путями к ним
from fixture.application import Application

fixture = None
target = None                                                               # Конфигурация запуска тестов

@pytest.fixture
def app(request):
    global fixture
    global target                                                           # Использование общей переменной
    browser = request.config.getoption("--browser")
    if target is None:                                                      # Если конфигурация не определена
        config_file = request.config.getoption("--target")                  # Определение пути к конфигурационному файлу
        if not os.path.isfile(config_file):                                 # Если задан не путь к файлу, а, например, только его имя
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))    # Определение пути к конфигурационному файлу по умолчанию
        with open(config_file) as f:                                        # Открыть файл, контроль автоматического закрытия после выполнения блока команд
            try:
                target = json.load(f)                                       # Загрузка данных из файла
            except ValueError as ex:                                        # В случае ошибки
                print(ex)                                                   # Вывод информации об ошибке
                target = None                                               # Сбросить данные конфигурации
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])       # Авторизация пользователя
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# Добавление использования параметров из командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


# Генератор тестов
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# Загрузка данных из модуля Python-а (файла .py) с заданным имененм
def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


# Загрузка данных из файла с заданным имененм
def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:    # Определение пути к конфигурационному файлу и его открытие
        return jsonpickle.decode(f.read())

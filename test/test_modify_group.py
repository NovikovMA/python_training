# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.group import Group                                               # Модель группы адресной книги


def test_modify_first_group_name(app):                                      # Тест возможности изменения группы
    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    app.group.modify_first_group(Group(name="New group"))                   # Изменение параметров первой в списке группы


def test_modify_first_group_header(app):                                    # Тест возможности изменения группы
    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    app.group.modify_first_group(Group(header="New header"))                # Изменение параметров первой в списке группы


def test_modify_first_group_footer(app):                                    # Тест возможности изменения группы
    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    app.group.modify_first_group(Group(footer="New footer"))                # Изменение параметров первой в списке группы

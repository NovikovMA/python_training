# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.group import Group                                               # Модель группы адресной книги


def test_edit_first_group(app):                                             # Тест возможности изменения группы
    app.session.login(username="admin", password="secret")                  # Авторизация пользователя
    app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    app.group.edit_first_group(Group(name="test edit group", header="Logo edit group", footer="Comment edit group"))    # Изменение параметров первой в списке группы
    app.session.logout()                                                    # Выход из программы

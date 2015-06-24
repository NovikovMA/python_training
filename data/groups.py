# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


from model.group import Group                                               # Модель группы контактов адресной книги


# Постоянные тестовые данные
testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

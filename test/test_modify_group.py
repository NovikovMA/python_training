# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.group import Group                                               # Модель группы адресной книги


def test_modify_first_group_name(app):                                      # Тест возможности изменения группы
    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)                                     # Изменение параметров первой в списке группы
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_first_group_header(app):                                    # Тест возможности изменения группы
#    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
#        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))                # Изменение параметров первой в списке группы
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_first_group_footer(app):                                    # Тест возможности изменения группы
#    if app.group.count() == 0:                                              # Проверка наличия хотябы одной группы в списке
#        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="New footer"))                # Изменение параметров первой в списке группы
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

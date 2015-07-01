# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.group import Group                                               # Модель группы адресной книги
from random import randrange                                                # Случайности


def test_modify_some_group(app, db, check_ui):                              # Тест возможности изменения группы
    if len(db.get_group_list()) == 0:                                       # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    old_groups = db.get_group_list()                                        # Получение списка групп
    index = randrange(len(old_groups))                                      # Получение случайного порядкового номера
    group = Group(name="New group")                                         # Изменяемая группа
    group.id = old_groups[index].id                                         # Установка идентификатора изменяемой группы
    app.group.modify_group_by_id(group)                                     # Изменение параметров группы
    new_groups = db.get_group_list()                                        # Получение измененного списка групп
    assert len(old_groups) == len(new_groups)                               # Проверка соответсвия длин списков групп до и после модификации элемента
    old_groups[index] = group                                               # Обновление старого списка групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

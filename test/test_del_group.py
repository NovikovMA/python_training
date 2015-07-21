# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.group import Group                                               # Модель группы контактов адресной книги
import pytest                                                               # Исполнение тестов
import random                                                               # Случайности


def test_delete_some_group(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):                # Отметка для отчета Allure
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    with pytest.allure.step('When I delete the group %s from the list' % group):    # Отметка для отчета Allure
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old list with the deleted group'): # Отметка для отчета Allure
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        with pytest.allure.step('Also check UI'):                           # Отметка для отчета Allure
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

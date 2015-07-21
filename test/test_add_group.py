# -*- coding: utf-8 -*-
from model.group import Group                                               # Модель группы контактов адресной книги
import pytest                                                               # Исполнение тестов


# Использование тестовых данных из py-файла
def test_add_group_data(app, db, check_ui, data_groups):
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = data_groups
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        with pytest.allure.step('Also check UI'):
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# Использование тестовых данных из json-файла
def test_add_group_json(app, db, check_ui, json_groups):
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = json_groups
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        with pytest.allure.step('Also check UI'):
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

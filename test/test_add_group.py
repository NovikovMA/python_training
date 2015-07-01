# -*- coding: utf-8 -*-
from model.group import Group                                               # Модель группы контактов адресной книги


# Использование тестовых данных из py-файла
def test_add_group_data(app, db, check_ui, data_groups):
    group = data_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# Использование тестовых данных из json-файла
def test_add_group_json(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:                                                            # Проверка необходимости дополнительной проверки пользовательского интерфейса
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

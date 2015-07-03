# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
from model.group import Group                                               # Модель группы адресной книги
import random                                                               # Случайности


# Тест добавления контакта в группу
def test_del_address_from_group(app, orm):
    if len(orm.get_group_list()) == 0:                                      # Проверка наличия хотябы одной группы в списке
        app.group.create(Group(name="test temp group", header="Logo temp group", footer="Comment temp group"))  # Создание группы на случай пустого списка групп
    groups = orm.get_group_list()                                           # Получение списка групп
    group = Group(name=random.choice(groups).name)                          # Получение случайного имени группы
    group = groups[list(sorted(groups, key=Group.id_or_max)).index(group)]  # Получение первой группы с именем (по идентификатору)
    group_index = app.group.get_group_list().index(Group(id=group.id, name=group.name.strip())) # Получение идентификатора по номеру группы
    if len(orm.get_addresses_in_group(group)) == 0:                         # Проверка наличия хотябы одного контакта в группе
        if len(orm.get_address_list()) == 0:                                # Проверка наличия хотябы одного контакта
            app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
        address = random.choice(orm.get_address_list())                     # Выбор контакта
        app.address.add_to_group_by_index([address], group_index)           # Добавление контактов в группу
    old_addresses_in_group = orm.get_addresses_in_group(group)              # Получение списка контактов группы
    count = 1                                                               # Количество контактов для удаления из группы (random.randrange(len(addresses_not_in_group)))
    address_list = [random.choice(old_addresses_in_group) for i in range(count)]    # Выбор контактов для добавления в группу
                                                                            # Исключение повторений контактов
    count = len(address_list)                                               # Количество контактов после исключения повторений
    app.address.del_from_group_by_index(address_list, group_index)          # Добавление контактов в группу
    new_addresses_in_group = orm.get_addresses_in_group(group)              # Получение  списка контактов группы, после добавления контакта
    assert len(old_addresses_in_group) - count == len(new_addresses_in_group)
    for address in address_list:                                            # Удаление контактов из старого списка группы
        old_addresses_in_group.remove(address)
    assert sorted(old_addresses_in_group, key=Address.id_or_max) == sorted(new_addresses_in_group, key=Address.id_or_max)

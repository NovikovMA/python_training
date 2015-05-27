# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):                                      # Изменение параметров первой группы
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_groups_page()                                             # Переход на страницу списка групп
        wd.find_element_by_name("selected[]").click()                       # Выбор первой в списке группы
        wd.find_element_by_name("edit").click()                             # Переход на страницу редактирования группы
        wd.find_element_by_name("group_name").click()                       # Выбрать поле "Group name"
        wd.find_element_by_name("group_name").clear()                       # Очистить поле
        wd.find_element_by_name("group_name").send_keys(group.name)         # Заполнить поле новым значение параметра
        wd.find_element_by_name("group_header").click()                     # Выбрать поле "Group header (Logo)"
        wd.find_element_by_name("group_header").clear()                     # Очистить поле
        wd.find_element_by_name("group_header").send_keys(group.header)     # Заполнить поле новым значение параметра
        wd.find_element_by_name("group_footer").click()                     # Выбрать поле "Group footer (Comment)"
        wd.find_element_by_name("group_footer").clear()                     # Очистить поле
        wd.find_element_by_name("group_footer").send_keys(group.footer)     # Заполнить поле новым значение параметра
        wd.find_element_by_name("update").click()                           # Подтверждение введенных параметров
        self.return_to_groups_page()                                        # Переход на страницу списка групп

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

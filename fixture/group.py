# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        if text is not None:                                                # Если изменяемое значение не пустое
            wd.find_element_by_name(field_name).click()                     # Выбрать поле
            wd.find_element_by_name(field_name).clear()                     # Очистить поле
            wd.find_element_by_name(field_name).send_keys(text)             # Заполнить поле новым значение параметра

    def fill_group_form(self, group):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    # Выбор первой в списке группы
    def select_first_group(self):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        wd.find_element_by_name("selected[]").click()                       # Выбор первой в списке группы

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()                                           # Выбор первой в списке группы
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_groups_page()                                             # Переход на страницу списка групп
        self.select_first_group()                                           # Выбор первой в списке группы
        # open modification form
        wd.find_element_by_name("edit").click()                             # Переход на страницу редактирования группы
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()                           # Подтверждение введенных параметров
        self.return_to_groups_page()                                        # Переход на страницу списка групп

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address


class AddressHelper:

    def __init__(self, app):
        self.app = app

    # Переход к списку контактов (главная страница)
    def open_address_page(self):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):    # При отсутсвии строки поиска
            wd.find_element_by_link_text("home").click()                    # Переход к списку контактов (главная страница)

    # Проверка и изменение полей-списков формы ввода
    def change_list_value(self, field_name, num, norma):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        if num is not None:                                                 # Если изменяемое значение не пустое
            if not wd.find_element_by_xpath(field_name + "[" + str(num + norma) + "]").is_selected():
                wd.find_element_by_xpath(field_name + "[" + str(num + norma) + "]").click()

    # Проверка и изменение текстовых полей формы ввода
    def change_text_value(self, field_name, text):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        if text is not None:                                                # Если изменяемое значение не пустое
            wd.find_element_by_name(field_name).click()                     # Выбрать поле
            wd.find_element_by_name(field_name).clear()                     # Очистить поле
            wd.find_element_by_name(field_name).send_keys(text)             # Заполнить поле новым значение параметра

    def fill_address_form(self, address):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.change_text_value("firstname", address.first_name)
        self.change_text_value("middlename", address.middle_name)
        self.change_text_value("lastname", address.last_name)
        self.change_text_value("nickname", address.nickname)
        self.change_text_value("title", address.title)
        self.change_text_value("company", address.company)
        self.change_text_value("address", address.address)
        self.change_text_value("home", address.tel_home)
        self.change_text_value("mobile", address.tel_mobile)
        self.change_text_value("work", address.tel_work)
        self.change_text_value("fax", address.tel_fax)
        self.change_text_value("email", address.web_email)
        self.change_text_value("email2", address.web_email2)
        self.change_text_value("email3", address.web_email3)
        self.change_text_value("homepage", address.web_homepage)
        # self.change_list_value(field_name, address.birthday_day, norma)
        # self.change_list_value(field_name, address.birthday_month, norma)
        self.change_text_value("byear", address.birthday_year)
        # self.change_list_value(field_name, address.anniversary_day, norma)
        # self.change_list_value(field_name, address.anniversary_month, norma)
        self.change_text_value("ayear", address.anniversary_year)
        self.change_text_value("address2", address.sec_address)
        self.change_text_value("phone2", address.home)
        self.change_text_value("notes", address.notes)

    # Создание нового контакта
    def create(self, address):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        # Запуск добавления нового контакта
        wd.find_element_by_link_text("add new").click()
        # Заполнение параметров контакта
        self.fill_address_form(address)
        self.change_list_value("//div[@id='content']/form/select[1]//option", address.birthday_day, 2)
        self.change_list_value("//div[@id='content']/form/select[2]//option", address.birthday_month, 1)
        self.change_list_value("//div[@id='content']/form/select[3]//option", address.anniversary_day, 2)
        self.change_list_value("//div[@id='content']/form/select[4]//option", address.anniversary_month, 1)
        # Подтверждение введенных данных
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.address_cache = None                                           # Сброс списка контактов

    # Выбор контакта из списка
    def select_address(self):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()        # Выбор контакта из списка

    def delete_address(self):                                               # Удаление контакта
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        self.select_address()                                               # Выбор контакта из списка
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()   # Подтверждение удаления
        self.address_cache = None                                           # Сброс списка контактов

    def modify_address(self, new_address_data):                             # Изменение параметров контакта
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        self.select_address()                                               # Выбор контакта
        # Заполнение параметров контакта
        self.fill_address_form(new_address_data)
        self.change_list_value("//div[@id='content']/form[1]/select[1]//option", new_address_data.birthday_day, 2)
        self.change_list_value("//div[@id='content']/form[1]/select[2]//option", new_address_data.birthday_month, 2)
        self.change_list_value("//div[@id='content']/form[1]/select[3]//option", new_address_data.anniversary_day, 2)
        self.change_list_value("//div[@id='content']/form[1]/select[4]//option", new_address_data.anniversary_month, 2)
        # Подтверждение изменений
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.address_cache = None                                           # Сброс списка контактов

    # Получение количества контактов в адресной книге
    def count(self):
        wd = self.app.wd                                                    # Получить доступ к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        return len(wd.find_elements_by_name("selected[]"))                  # Колическво возможных к выбору элементов списка

    address_cache = None                                                    # Список контактов

    # Получение списка контактов
    def get_address_list(self):
        if self.address_cache is None:                                      # При отсутствии списка групп
            wd = self.app.wd                                                    # Получить доступ к web-драйверу
            self.open_address_page()                                            # Переход к списку контактов (главная страница)
            self.address_cache = []                                             # Изначально список контактов пустой
            for element in wd.find_elements_by_name("entry"):                   # Перебор всех элементов списка на странице
                id = element.find_element_by_name("selected[]").get_attribute("id")  # Получение идентификатора контакта
                last_name = element.find_elements_by_tag_name("td")[1].text     # Получение фамилии контакта
                first_name = element.find_elements_by_tag_name("td")[2].text    # Получение имени контакта
                self.address_cache.append(Address(id=id, last_name=last_name, first_name=first_name))    # Добавление в список контактов
        return list(self.address_cache)                                         # Список контактов

# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address
import re


class AddressHelper:

    def __init__(self, app):
        self.app = app

    # Переход к списку контактов (главная страница)
    def open_address_page(self):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
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
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
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
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
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

    # Выбор первого контакта из списка
    def select_address(self):
        self.select_address_by_index(0)

    # Открытие страницы редактирования контакта
    def select_address_by_index(self, index):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()  # Выбор контакта из списка

    # Удаление первого контакта
    def delete_address(self):
        self.delete_address_by_index(0)                                     # Удаление контакта

    # Удаление контакта
    def delete_address_by_index(self, index):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        self.select_address_by_index(index)                                 # Выбор контакта из списка
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()   # Подтверждение удаления
        self.address_cache = None                                           # Сброс списка контактов

    # Изменение параметров первого в списке контакта
    def modify_address(self, new_address_data):
        self.modify_address_by_index(0, new_address_data)

    # Изменение параметров контакта
    def modify_address_by_index(self, index, new_address_data):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        self.select_address_by_index(index)                                 # Выбор контакта из списка
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
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        return len(wd.find_elements_by_name("selected[]"))                  # Колическво возможных к выбору элементов списка

    address_cache = None                                                    # Список контактов

    # Получение списка контактов
    def get_address_list(self):
        if self.address_cache is None:                                      # При отсутствии списка групп
            wd = self.app.wd                                                # Получение доступа к web-драйверу
            self.open_address_page()                                        # Переход к списку контактов (главная страница)
            self.address_cache = []                                         # Изначально список контактов пустой
            for row in wd.find_elements_by_name("entry"):                   # Перебор всех элементов списка на странице
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("id")    # Получение идентификатора контакта
                last_name = cells[1].text                                   # Получение фамилии контакта
                first_name = cells[2].text                                  # Получение имени контакта
                address = cells[3].text                                     # Получение адреса контакта
                all_email = "\n".join(map(lambda x: x.text,
                                          cells[4].find_elements_by_tag_name("a")))  # Получение списка адресов эл.почты контакта
                all_phones = cells[5].text                                  # Получение списка телефонов
                self.address_cache.append(Address(id=id, last_name=last_name, first_name=first_name,
                                                  address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))  # Добавление в список контактов
        return list(self.address_cache)                                     # Список контактов

    # Открытие страницы подробной информации о контакте
    def open_address_view_by_index(self, index):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        row = wd.find_elements_by_name("entry")[index]                      # Выбор контакта из списка
        cell = row.find_elements_by_tag_name("td")[6]                       # Поиск кнопки просмотра информации
        cell.find_element_by_tag_name("a").click()                          # Нажатие кнопки просмотра информации о контакте

    # Получение информации о контакте со страницы редактирования
    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_page()                                            # Переход к списку контактов (главная страница)
        self.select_address_by_index(index)                                 # Открытие страницы редактирования контакта
        id = wd.find_element_by_name("id").get_attribute("value")           # Получение идентификатора контакта
        first_name = wd.find_element_by_name("firstname").get_attribute("value")    # Получение имени контакта
        last_name = wd.find_element_by_name("lastname").get_attribute("value")  # Получение фамилии контакта
        address = wd.find_element_by_name("address").text                   # Получение адреса контакта
        home_phone = wd.find_element_by_name("home").get_attribute("value") # Получение домашнего телефона контакта
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value") # Получение мобильного телефона контакта
        work_phone = wd.find_element_by_name("work").get_attribute("value") # Получение рабочего телефона контакта
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")  # Получение дополнительного телефона контакта
        web_email = wd.find_element_by_name("email").get_attribute("value") # Получение домашнего телефона контакта
        web_email2 = wd.find_element_by_name("email2").get_attribute("value")   # Получение мобильного телефона контакта
        web_email3 = wd.find_element_by_name("email3").get_attribute("value")   # Получение рабочего телефона контакта
        return Address(id=id, first_name=first_name, last_name=last_name,
                       address=address,
                       tel_home=home_phone, tel_mobile=mobile_phone,
                       tel_work=work_phone, home=secondary_phone,
                       web_email=web_email, web_email2=web_email2, web_email3=web_email3)    # Контакт

    # Получение информации о контакте со страницы подробной информации
    def get_address_info_from_view_page(self, index):
        wd = self.app.wd                                                    # Получение доступа к web-драйверу
        self.open_address_view_by_index(index)                              # Открытие страницы подробной информации о контакте
        address_text = wd.find_element_by_id("content").text                # Получение текстовой подробной информации о контекте
        home_phone = re.search("H: (.*)", address_text).group(1)            # Получение домашнего телефона контакта
        mobile_phone = re.search("M: (.*)", address_text).group(1)          # Получение мобильного телефона контакта
        work_phone = re.search("W: (.*)", address_text).group(1)            # Получение рабочего телефона контакта
        secondary_phone = re.search("P: (.*)", address_text).group(1)       # Получение дополнительного телефона контакта
        return Address(tel_home=home_phone, tel_mobile=mobile_phone,
                       tel_work=work_phone, home=secondary_phone)           # Контакт

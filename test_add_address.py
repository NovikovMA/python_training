# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from address import Address

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_address(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    # Открыть программу в окне браузера
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    # Авторизация пользователя
    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    # Заполнение полей параметров контакта
    def create_address(self, wd, address):
        # Запуск добавления нового контакта
        wd.find_element_by_link_text("add new").click()
        # Заполнение параметров контакта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(address.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(address.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(address.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(address.tel_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.tel_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(address.tel_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(address.tel_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.web_email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(address.web_email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(address.web_email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(address.web_homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(address.birthday_day + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + str(address.birthday_day + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(address.birthday_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + str(address.birthday_month + 1) + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(address.birthday_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(address.anniversary_day + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + str(address.anniversary_day + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(address.anniversary_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + str(address.anniversary_month + 1) + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(address.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address.sec_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(address.home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(address.notes)
        # Подтверждение введенных данных
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    # Выход из программы
    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_address(self):
        wd = self.wd
        self.open_home_page(wd)                                             # Открыть программу в окне браузера
        self.login(wd, "admin", "secret")                                   # Авторизация пользователя
        self.create_address(wd, Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes"))                                  # Заполнение полей параметров контакта
        self.logout(wd)                                                     # Выход из программы

    def test_add_empty_address(self):
        wd = self.wd
        self.open_home_page(wd)                                             # Открыть программу в окне браузера
        self.login(wd, "admin", "secret")                                   # Авторизация пользователя
        self.create_address(wd, Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", tel_home="", tel_mobile="", tel_work="", tel_fax="", web_email="", web_email2="", web_email3="", web_homepage="", birthday_day=0, birthday_month=0, birthday_year="", anniversary_day=0, anniversary_month=0, anniversary_year="", sec_address="", home="", notes=""))                                  # Заполнение полей параметров контакта
        self.logout(wd)                                                     # Выход из программы

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

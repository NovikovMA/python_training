# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    # Авторизация пользователя
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()                                           # Открыть программу в окне браузера
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    # Выход из программы
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():                                             # Если пользователь авторизован
            if self.is_logged_in_as(username):                              # Если пользователь авторизован не под своим именем
                return
            else:
                self.logout()
        self.login(username, password)                                      # Авторизация пользователя

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

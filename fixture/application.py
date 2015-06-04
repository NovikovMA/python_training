# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from fixture.address import AddressHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.address = AddressHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    # Открыть программу в окне браузера
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

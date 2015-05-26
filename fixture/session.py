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

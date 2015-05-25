from selenium.webdriver.firefox.webdriver import WebDriver
__author__ = 'M.Novikov'


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    # ������� ��������� � ���� ��������
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # ����������� ������������
    def login(self, username, password):
        wd = self.wd
        self.open_home_page()                                               # ������� ��������� � ���� ��������
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    # ���������� ����� ���������� ��������
    def create_address(self, address):
        wd = self.wd
        # ������ ���������� ������ ��������
        wd.find_element_by_link_text("add new").click()
        # ���������� ���������� ��������
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
        # ������������� ��������� ������
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    # ����� �� ���������
    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
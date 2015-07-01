# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from sys import maxsize


class Address:

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None,
                 nickname=None, title=None, company=None, address=None,
                 tel_home=None, tel_mobile=None, tel_work=None, tel_fax=None,
                 web_email=None, web_email2=None, web_email3=None, web_homepage=None,
                 birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None,
                 sec_address=None, home=None, notes=None,
                 all_phones_from_home_page=None, all_email_from_home_page=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.tel_home = tel_home
        self.tel_mobile = tel_mobile
        self.tel_work = tel_work
        self.tel_fax = tel_fax
        self.web_email = web_email
        self.web_email2 = web_email2
        self.web_email3 = web_email3
        self.web_homepage = web_homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.sec_address = sec_address
        self.home = home
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.first_name == other.first_name\
               and self.last_name == other.last_name\
               and self.address == other.address\
               and (self.all_phones_from_home_page is None or other.all_phones_from_home_page is None or self.all_phones_from_home_page == other.all_phones_from_home_page)\
               and (self.all_email_from_home_page is None or other.all_email_from_home_page is None or self.all_email_from_home_page == other.all_email_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги


def test_edit_address(app):                                                 # Тест изменения контакта
    app.session.login(username="admin", password="secret")                  # Авторизация пользователя
    app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
    app.address.edit_address(Address(first_name="Александр", middle_name="Александрович", last_name="Падерин", nickname="A.Paderin", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-18-65", tel_mobile="002-18-65", tel_work="003-18-65", tel_fax="004-18-65", web_email="", web_email2="A.Paderin@systema.biz", web_email3="A.Paderin@dors.com", web_homepage="http://software-testing.ru", birthday_day=4, birthday_month=11, birthday_year="1984", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes"))          # Изменение параметров контакта
    app.session.logout()                                                    # Выход из программы

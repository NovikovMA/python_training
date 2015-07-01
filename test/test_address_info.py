# -*- coding: utf-8 -*-
__author__ = 'M.Novikov'

from model.address import Address                                           # Модель контакта адресной книги
#from random import randrange                                                # Случайности
import re                                                                   # Регулярные выражения


# Тест сравнения списков контактов, полученных из базы данных и через пользовательский интерфейс главной страницы
def test_address_list_info_on_home_page(app, db):
    def clean_address_db(address):                                          # Преобразование формата данных, полученных из базы, в формат пользовательского интерфейса
        id = str(address.id)                                                # Идентификатор пользователя
        first_name = re.sub(r' {2,}', ' ', address.first_name).strip()      # Имя контакта
        last_name = re.sub(r' {2,}', ' ', address.last_name).strip()        # Фамилия контакта
        adres = re.sub(r'\r', '', re.sub(r' {2,}', ' ', address.address)).strip()   # Адресс контакта
        all_phones = merge_phones_like_on_home_page(address)                # Набор телефонов контакта
        all_email = merge_email_like_on_home_page(address)                  # Набор адресов электронных почт контакта
        return Address(id=id,
                       first_name=first_name, last_name=last_name,
                       address=adres,
                       all_phones_from_home_page=all_phones,
                       all_email_from_home_page=all_email)                  # Модифицированная для сравнения контактов
    db_list = list(map(clean_address_db, db.get_address_list()))            # Список контактов из базы данных, без начинающих и завершающих пробелов, приведенные к строковоку формату
    ui_list = app.address.get_address_list()                                # Список контактов с экрана
    assert sorted(db_list, key=Address.id_or_max) == sorted(ui_list, key=Address.id_or_max)


# Тест сравнения списков контактов, полученных из базы данных и через пользовательский интерфейс страницы редактирования контактов
def test_address_list_info_on_edit_page(app, db):
    def clean_address_db(address):                                          # Преобразование формата данных, полученных из базы, в формат пользовательского интерфейса
        id = str(address.id)                                                # Идентификатор пользователя
        first_name = address.first_name                                     # Имя контакта
        last_name = address.last_name                                       # Фамилия контакта
        adres = re.sub(r'\r', '', address.address)                          # Адресс контакта
        return Address(id=id,
                       first_name=first_name, last_name=last_name,
                       address=adres)                                       # Модифицированная для сравнения контактов
    db_list = list(map(clean_address_db, db.get_address_list()))            # Список контактов из базы данных, без начинающих и завершающих пробелов, приведенные к строковоку формату
    ui_list = app.address.get_address_list_from_edit_page()                 # Список контактов с экрана
    assert sorted(db_list, key=Address.id_or_max) == sorted(ui_list, key=Address.id_or_max)


# Тест сравнения информации о контакте главной страницы и формы редактирования
#def test_address_info_on_home_page(app, db):
#    if len(db.get_address_list()) == 0:                                     # Проверка наличия хотябы одного контакта в списке
#        app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
#    addresses = db.get_address_list()                                       # Получение списка контактов
#    index = randrange(len(addresses))                                       # Получение случайного порядкового номера
#    address_from_home_page = app.address.get_address_list()[index]          # Получение контакта из списка
#    address_from_edit_page = app.address.get_address_info_from_edit_page(index)  # Получение контакта со страницы редактирования
#    assert address_from_home_page.last_name == address_from_edit_page.last_name  # Проверка соответсвия фамилии контакта
#    assert address_from_home_page.first_name == address_from_edit_page.first_name   # Проверка соответсвия имени контакта
#    assert address_from_home_page.address == address_from_edit_page.address # Проверка соответсвия адреса контакта
#    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)   # Проверка соответсвия телефонов контакта
#    assert address_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(address_from_edit_page)     # Проверка соответсвия адресов эл. почты контакта


# Тест сравнения информации о контакте главной страницы и формы редактирования без проверки начальных пар нулей
#def test_phone_info_on_home_page_without_check_00(app):
#    if app.address.count() == 0:                                            # Проверка наличия хотябы одного контакта в списке
#        app.address.create(Address(first_name="Михаил", middle_name="Алексеевич", last_name="Новиков", nickname="M.Novikov", title="Title", company="КБ ДОРС", address="Федеративный пр. д.15 к.4", tel_home="001-13-59", tel_mobile="002-13-59", tel_work="003-13-59", tel_fax="004-13-59", web_email="malnovikov@yandex.ru", web_email2="M.Novikov@systema.biz", web_email3="M.Novikov@dors.com", web_homepage="http://software-testing.ru", birthday_day=14, birthday_month=11, birthday_year="1986", anniversary_day=1, anniversary_month=1, anniversary_year="2000", sec_address="Secondary Address", home="Home", notes="Notes")) # Создание контакта на случай пустого списка
#    addresses = app.address.get_address_list()                              # Получение списка контактов
#    index = randrange(len(addresses))                                       # Получение случайного порядкового номера
#    address_from_home_page = app.address.get_address_list()[index]          # Получение контакта из списка
#    address_from_edit_page = app.address.get_address_info_from_edit_page(index) # Получение контакта со страницы редактирования
#    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page_without_00(address_from_edit_page)


#def test_address_info_on_address_view_page(app):
#    address_from_view_page = app.address.get_address_info_from_view_page(0) # Получение контакта со страницы подробной инфомации
#    address_from_edit_page = app.address.get_address_info_from_edit_page(0) # Получение контакта со страницы редактирования
#    assert address_from_view_page.tel_home == address_from_edit_page.tel_home    # Проверка соответсвия номера телефона
#    assert address_from_view_page.tel_mobile == address_from_edit_page.tel_mobile    # Проверка соответсвия номера телефона
#    assert address_from_view_page.tel_work == address_from_edit_page.tel_work    # Проверка соответсвия номера телефона
#    assert address_from_view_page.sec_address == address_from_edit_page.sec_address  # Проверка соответсвия номера телефона


# Замена символов в строке
def clear(s):
    return re.sub("[() -]", "", s)


# Замена начальных пар нулей
def clear_00(s):
    if s.startswith("00"):
        return "+" + s[2:]
    return s


# Объединение телефонов в одну строку с приведением к виду главной страницы
def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                map(lambda x: clear_00(x),
                                    filter(lambda x: x is not None,
                                           [address.tel_home, address.tel_mobile, address.tel_work, address.home])))))


# Объединение телефоновв одну строку с неполным приведением к виду главной страницы
def merge_phones_like_on_home_page_without_00(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address.tel_home, address.tel_mobile, address.tel_work, address.home]))))


# Объединение адресов электронной почты в одну строку
def merge_email_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x.strip(),
                                filter(lambda x: x is not None,
                                       [address.web_email, address.web_email2, address.web_email3]))))

from selenium import webdriver
from url import Urls
import pytest
import random

@pytest.fixture
def test_user_data():
    list_domen = ['ya.ru', 'gmail.com', 'mail.ru']
    password = str(random.randint(100000, 999999))
    email = 'Ivan_Hritankov_25_' + str(random.randint(100, 999)) + '@' + random.choice(list_domen)
    name = 'Иван' + password

    return {
        'email': email,
        'password': password,
        'name': name
    }

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.MAIN_URL)

    yield driver

    driver.quit()

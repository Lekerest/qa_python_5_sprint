from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_registration(driver, test_user_data):

    ### Сначала фикстура driver ###

    ### Создаем пользовательские данные ###
    email = test_user_data['email']
    password = test_user_data['password']
    name = test_user_data['name']

    ### Ждем копку личный кабинет и нажимаем ###
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET))
    driver.find_element(Locators.BUTTON_PERSONAL_CABINET).click()

    ### Ждем кнопку зарегистрироваться и нажимаем ###
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN))
    driver.find_element(Locators.TEXT_REGISTRATION_LOGIN).click()

    ### Ждем поле с именем и вводим данные в каждое поле после нажимаем зарегистрироваться ###
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.FIELD_NAME))
    driver.find_element(Locators.FIELD_NAME).send_keys(name) ### имя
    driver.find_element(Locators.FIELD_EMAIL).send_keys(email) ### email
    driver.find_element(Locators.FIELD_PASSWORD).send_keys(password) ### пароль
    driver.find_element(Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click() ### кнопка зарегистрироваться

    ### Ждем форму входа, заполняем и нажимаем войти ###
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.FIELD_EMAIL))
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FIELD_EMAIL))
    driver.find_element(Locators.FIELD_EMAIL).send_keys(email) ### email
    driver.find_element(Locators.FIELD_PASSWORD).send_keys(password) ### пароль
    driver.find_element(Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()

    ### Ждем копку личный кабинет и нажимаем ###
    #WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET))
    #driver.find_element(Locators.BUTTON_PERSONAL_CABINET).click()

#    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
#        (By.XPATH, "html/body/div/div/header/nav/a[@class='AppHeader_header__link__3D_hX']")))
#    driver.find_element(By.XPATH, ".//p[(@class='AppHeader_header__linkText__3q_va ml-2') and (text()='Личный Кабинет')]").click()

    assert driver.current_url == Locators.MAIN_URL
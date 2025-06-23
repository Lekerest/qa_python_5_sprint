from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from Tests.Data.data_users import valid_user
from url import Urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

def authorization(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
    login_in_account(driver)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()

def login_in_account(driver):
    email = valid_user["email"]
    password = valid_user["password"]
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIELD_EMAIL))
    driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)  ### email
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)  ### пароль
    driver.find_element(*Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Urls.MAIN_URL))

def register_user(driver, name, email, password):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN)).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.FIELD_NAME))
    driver.find_element(*Locators.FIELD_NAME).send_keys(name)
    driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()
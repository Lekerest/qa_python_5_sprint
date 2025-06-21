from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def login_in_account(driver):
    email = "test@testtest.ru"
    password = 123456
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FIELD_EMAIL))
    driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)  ### email
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)  ### пароль
    driver.find_element(*Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Locators.MAIN_URL))

class TestLogin:

############ 1. Вход по кнопке с главной страницы ############
    def test_login_log_in_to_your_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_ACCOUNT_ON_MAIN_PAGE)).click()
        login_in_account(driver)
        assert driver.current_url == Locators.MAIN_URL

############ 2. Вход по кнопке из личного кабинета ############
    def test_login_personal_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        login_in_account(driver)
        assert driver.current_url == Locators.MAIN_URL

############ 3. Вход по кнопке из регистрации ############
    def test_login_from_registration_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_ACCOUNT_FROM_REGISTRATION)).click()
        login_in_account(driver)
        assert driver.current_url == Locators.MAIN_URL

############ 4. Вход по кнопке из восстановления пароля ############
    def test_login_from_recovery_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_RECOVERY_PASSWORD)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_RECOVERY_FORM)).click()
        login_in_account(driver)
        assert driver.current_url == Locators.MAIN_URL

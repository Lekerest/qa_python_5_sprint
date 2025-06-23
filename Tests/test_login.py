from helpers import *

class TestLogin:

############ 1. Вход по кнопке с главной страницы ############
    def test_login_log_in_to_your_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_ACCOUNT_ON_MAIN_PAGE)).click()
        login_in_account(driver)
        assert driver.current_url == Urls.MAIN_URL

############ 2. Вход по кнопке из личного кабинета ############
    def test_login_personal_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        login_in_account(driver)
        assert driver.current_url == Urls.MAIN_URL

############ 3. Вход по кнопке из регистрации ############
    def test_login_from_registration_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_ACCOUNT_FROM_REGISTRATION)).click()
        login_in_account(driver)
        assert driver.current_url == Urls.MAIN_URL

############ 4. Вход по кнопке из восстановления пароля ############
    def test_login_from_recovery_form(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_RECOVERY_PASSWORD)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_RECOVERY_FORM)).click()
        login_in_account(driver)
        assert driver.current_url == Urls.MAIN_URL

from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from test_login import login_in_account

class TestWebPageCrossing:

############ 1. Нажатие на личный кабинет у авторизованного пользователя переводит в личный кабинет ############
    def test_crossing_on_personal_cabinet(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        login_in_account(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Locators.PERSONAL_CABINET_URL))
        assert driver.current_url == Locators.PERSONAL_CABINET_URL

############ 2. Переход из личного кабинета на главную через лого ############
    def test_login_personal_account(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        login_in_account(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_URL)).click()
        assert driver.current_url == Locators.MAIN_URL


# ############ 3. Вход по кнопке из регистрации ############
#     def test_login_from_registration_form(self, driver):
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN)).click()
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_ACCOUNT_FROM_REGISTRATION)).click()
#         login_in_account(driver)
#
# ############ 4. Вход по кнопке из восстановления пароля ############
#     def test_login_from_recovery_form(self, driver):
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_RECOVERY_PASSWORD)).click()
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_RECOVERY_FORM)).click()
#         login_in_account(driver)

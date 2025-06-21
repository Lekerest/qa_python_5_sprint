from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .test_login import login_in_account

def authorization(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
    login_in_account(driver)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()

class TestWebPageCrossing:

############ 1. Нажатие на личный кабинет у авторизованного пользователя переводит в личный кабинет ############
    def test_crossing_on_personal_cabinet(self, driver):
        authorization(driver)
        WebDriverWait(driver, 5).until(EC.url_to_be(Locators.PERSONAL_CABINET_URL))
        assert driver.current_url == Locators.PERSONAL_CABINET_URL

############ 2. Переход из личного кабинета на главную через лого ############
    def test_crossing_on_main_page_through_logo(self, driver):
        authorization(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_URL)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Locators.MAIN_URL))
        assert driver.current_url == Locators.MAIN_URL

############ 3. Переход из личного кабинета на главную через текст конструктор ############
    def test_crossing_on_main_page_through_constructor(self, driver):
        authorization(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_CONSTRUCTOR_URl)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Locators.MAIN_URL))
        assert driver.current_url == Locators.MAIN_URL

############ 4. Выход из аккаунта ############
    def test_exit_from_account(self, driver):
        authorization(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_EXIT_FROM_ACCOUNT)).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(Locators.LOGIN_FORM_URL))
        assert driver.current_url == Locators.LOGIN_FORM_URL

############ 5. Переход к разделу булки ############
    def test_crossing_chapter_buns(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_BUTTON_SAUCE)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_BUTTON_BUNS)).click()
        element = driver.find_element(*Locators.POSITION_KRATORNAYA_BUN)
        assert element.is_displayed(), "Элемент POSITION_KRATORNAYA_BUN не отображается на экране"

############ 6. Переход к разделу соусы ############
    def test_crossing_chapter_sauce(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_BUTTON_SAUCE)).click()
        element = driver.find_element(*Locators.POSiTION_ANTARIAN_FLATWALKER_SPIKED_SAUCE)
        assert element.is_displayed(), "Элемент POSiTION_ANTARIAN_FLATWALKER_SPIKED_SAUCE не отображается на экране"

############ 7. Переход к разделу начинки ############
    def test_crossing_chapter_fillings(self, driver):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.TEXT_BUTTON_FILLINGS)).click()
        element = driver.find_element(*Locators.POSITION_CHEESE_WITH_ASTEROID_MOLD)
        assert element.is_displayed(), "Элемент POSITION_CHEESE_WITH_ASTEROID_MOLD не отображается на экране"

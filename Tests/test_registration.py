from locators import Locators
from url import Urls
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def register_user(driver, name, email, password):
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_PERSONAL_CABINET)).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.TEXT_REGISTRATION_LOGIN)).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.FIELD_NAME))
    driver.find_element(*Locators.FIELD_NAME).send_keys(name)
    driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)
    driver.find_element(*Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()

class TestRegistration:

    def test_registration(self, driver, test_user_data):
        email = test_user_data['email']
        password = test_user_data['password']
        name = test_user_data['name']

        register_user(driver, name, email, password)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_ENTRANCE_IN_LOGIN_FORM))
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email) ### email
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password) ### пароль
        driver.find_element(*Locators.BUTTON_REGISTRATION_FORM_AND_ENTRANCE).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(Urls.MAIN_URL))
        assert driver.current_url == Urls.MAIN_URL

    def test_password_error(self, driver, test_user_data):
        email = test_user_data['email']
        password = 12345
        name = test_user_data['name']

        register_user(driver, name, email, password)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ERROR_PASSWORD))
        assert "Некорректный пароль" == driver.find_element(*Locators.ERROR_PASSWORD).text

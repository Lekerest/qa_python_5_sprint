from selenium.webdriver.common.by import By
class Locators:
    #Главная страница
    MAIN_URL = "https://stellarburgers.nomoreparties.site/"

    #Личный кабинет
    BUTTON_PERSONAL_CABINET = (By.XPATH, "html/body/div/div/header/nav/a[@class='AppHeader_header__link__3D_hX']")

    #Кнопка зарегистрироваться как текст в форме войти
    TEXT_REGISTRATION_LOGIN = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    #Поле имя
    FIELD_NAME = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Имя']/following-sibling::input")

    #Поле email
    FIELD_EMAIL = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Email']/following-sibling::input")

    #Поле пароль
    FIELD_PASSWORD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/*[text()='Пароль']/following-sibling::input")

    #Кнопка зарегистрироваться в форме регистрации
    BUTTON_REGISTRATION_FORM_AND_ENTRANCE = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")

    #Некорректный пароль
    ERROR_PASSWORD = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

    #Кнопка входа с главной страницы
    BUTTON_ENTRANCE_IN_ACCOUNT = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")


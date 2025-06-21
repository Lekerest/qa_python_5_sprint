from selenium.webdriver.common.by import By
class Locators:
    #Главная страница
    MAIN_URL = "https://stellarburgers.nomoreparties.site/"

    #Страница личный кабинет
    PERSONAL_CABINET_URL = "https://stellarburgers.nomoreparties.site/account/profile"

    #Страница входа
    LOGIN_FORM_URL = "https://stellarburgers.nomoreparties.site/login"

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
    BUTTON_ENTRANCE_IN_ACCOUNT_ON_MAIN_PAGE = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")

    #Кнопка входа из формы регистрации
    BUTTON_ENTRANCE_IN_ACCOUNT_FROM_REGISTRATION = (By.CSS_SELECTOR, ".Auth_link__1fOlj")

    # Кнопка восстановления пароля
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, ".//a[(@class='Auth_link__1fOlj') and (text()='Восстановить пароль')]")

    #Кнопка входа из формы восстановления пароля
    BUTTON_ENTRANCE_IN_RECOVERY_FORM = (By.CSS_SELECTOR, ".Auth_link__1fOlj")

    #Переход по логотипу
    LOGO_URL = (By.XPATH, ".//a[(@href='/')]")

    #Кликабельный текст Конструктор
    TEXT_CONSTRUCTOR_URl = (By.CSS_SELECTOR, '.AppHeader_header__linkText__3q_va.ml-2')

    #Кнопка выхода из аккаунта
    BUTTON_EXIT_FROM_ACCOUNT = (By.CSS_SELECTOR, ".Account_button__14Yp3.text.text_type_main-medium.text_color_inactive")

    #Кликабельный текст Булки
    TEXT_BUTTON_BUNS = (By.XPATH, ".//span[(@class='text text_type_main-default') and (text()='Булки')]")

    #Кликабельный текст Соусы
    TEXT_BUTTON_SAUCE = (By.XPATH, ".//span[(@class='text text_type_main-default') and (text()='Соусы')]")

    #Кликабельный текст Начинки
    TEXT_BUTTON_FILLINGS = (By.XPATH, ".//span[(@class='text text_type_main-default') and (text()='Начинки')]")

    #Булка краторная N-200i
    POSITION_KRATORNAYA_BUN = (By.XPATH, ".//*[(text()='Краторная булка N-200i')]")

    #Соус с шипами Антарианского плоскоходца
    POSiTION_ANTARIAN_FLATWALKER_SPIKED_SAUCE = (By.XPATH, ".//*[(text()='Соус с шипами Антарианского плоскоходца')]")

    #Сыр с астероидной плесенью
    POSITION_CHEESE_WITH_ASTEROID_MOLD = (By.XPATH, ".//*[(text()='Сыр с астероидной плесенью')]")

    #Надпись вход в форме входа
    INSCRIPTION_ENTRANCE = (By.XPATH, ".//h2[(text()='Вход')]")

    #Кнопка войти в форме входа
    BUTTON_ENTRANCE_IN_LOGIN_FORM = (By.XPATH, ".//button[(@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa') and (text()='Войти')]")
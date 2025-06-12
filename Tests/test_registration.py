import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

def test_registration():
    driver = webdriver.Chrome()
    driver.maximize_window() # полноэкранный режим
    driver.get("https://stellarburgers.nomoreparties.site/") ### главная страница сайта

    list_domen = ['ya.ru', 'gmail.com', 'mail.ru']
    Email = 'Ivan_Hritankov_25_' + str(random.randint(100, 999)) + '@' + random.choice(list_domen) ### Email
    password = str(random.randint(100000, 999999)) ### пароль
    name = 'Иван' + str(password) ### имя


    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "html/body/div/div/header/nav/a[@class='AppHeader_header__link__3D_hX']")))
    driver.find_element(By.XPATH, "html/body/div/div/header/nav/a[@class='AppHeader_header__link__3D_hX']").click() ### личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//a[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() ### кнопка зарегистрироваться


    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
        (By.XPATH,
         ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Имя']/following-sibling::input")))

    driver.find_element(By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Имя']/following-sibling::input").send_keys(name) ### имя
    driver.find_element(By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Email']/following-sibling::input").send_keys(Email) ### Email
    driver.find_element(By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/*[text()='Пароль']/following-sibling::input").send_keys(password) ### пароль

    driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() ### кнопка зарегистрироваться

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/*[text()='Пароль']/following-sibling::input")))
    time.sleep(2)
    driver.find_element(By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Email']/following-sibling::input").send_keys(Email) ### Email
    driver.find_element(By.XPATH,
    ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/*[text()='Пароль']/following-sibling::input").send_keys(password) ### пароль
    driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()


    time.sleep(2)
    driver.quit()
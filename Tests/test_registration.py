import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window() # полноэкранный режим
driver.get("https://stellarburgers.nomoreparties.site/")

login = 'Ivan_Hritankov_25_' + str(random.randint(99, 1000))
password = random.randint(100000, 999999)


driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    #Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(element.text)
    y = calc(x)
    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
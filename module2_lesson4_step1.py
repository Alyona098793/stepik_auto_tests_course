from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

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
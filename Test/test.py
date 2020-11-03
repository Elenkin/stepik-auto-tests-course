from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome('')
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100')
                                     )
    # Нажать на кнопку "Book"
    browser.find_element_by_id("book").click()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # Нажать на кнопку Submit
    browser.find_element_by_id("solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Лучше использовать лимит ожидания browser.implicitly_wait('время ожидания') перед browser.get()
    # закрываем браузер после всех манипуляций
    browser.quit()
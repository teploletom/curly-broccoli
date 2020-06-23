from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	# Нажимаем на кнопку I want to go on...
    button = browser.find_element_by_css_selector("button.btn")
    time.sleep(3)	
    button.click()		
	
	# Возьмем вкладку методом и запишим в переменную. Переключиться на новую вкладку, указав ее явно.
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)	
	
    # Находим строку где содержится Х из формулы
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)	

    # Записываем в форму найденный у
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)	

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
	

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
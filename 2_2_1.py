from selenium import webdriver #
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	
    # Находим нужную строку, вторая строка вытаскиваем текст, который является нужным числом
    input1 = browser.find_element_by_id("num1")
    x1 = input1.text	
    input2 = browser.find_element_by_id("num2")
    x2 = input2.text	
    y = str(int(x1) + int(x2))	
	
	#Первое решение
   # browser.find_element_by_tag_name("select").click()
   # browser.find_element_by_css_selector("[value='" + y + "']").click()
	
	#Второе решение
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
   # Select(browser.find_element_by_tag_name("select")).select_by_value(y)
	
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
#except Exception as error:
 #   print(f'Произошла ошибка, вот её трэйсбэк: {error}')
	

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
   # browser.close()	
  #  browser.quit()
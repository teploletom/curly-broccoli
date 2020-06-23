from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# ищем price
#price = browser.find_element_by_id("price")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id("book")	
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

# Отправляем заполненную форму
button2 = browser.find_element_by_css_selector("button.btn")
button2.click()

alert = browser.switch_to.alert
alert_text = alert.text
print(alert.text)
	
#message = browser.find_element_by_id("verify_message")

#assert "successful" in message.text
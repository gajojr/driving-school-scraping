from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://servisi.euprava.gov.rs/autoskole/prijava")
username_input = driver.find_element_by_id('IdNumber')
password_input = driver.find_element_by_id('Password')
user_login_button = driver.find_element_by_class_name('btn-primary')

print(username_input.get_attribute('placeholder'))
print(password_input.get_attribute('placeholder'))
print(user_login_button.text)

username_input.send_keys('your_id')
password_input.send_keys('your_password')
user_login_button.submit()
# with open('data.txt', 'w') as file:
#     for idx in range(0, len(code)):
#         if code[idx].text[0] != '/':
#             file.write(code[idx].text)
#             file.write('\n\n')


# time.sleep(5)
# driver.quit()

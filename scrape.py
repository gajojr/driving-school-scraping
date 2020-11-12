from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://servisi.euprava.gov.rs/autoskole/prijava")

# login part
username_input = driver.find_element_by_id('IdNumber')
password_input = driver.find_element_by_id('Password')
user_login_button = driver.find_element_by_class_name('btn-primary')

# send data to inputs and submit the form
username_input.send_keys('****************')
password_input.send_keys('************')
user_login_button.submit()

# select menu
side_menu = driver.find_element_by_class_name('menu-text')
side_menu.click()

# select teory practice from side-bar menu
teory_practice_submenu = driver.find_elements_by_class_name('icon-angle-down')
# in submenu there are 5 links that have down arrow icon and teory practice is at second place
# there is no better way to select because there are no ids for links only classes which are same for all links
teory_practice_submenu[1].click()

# go to teory practice panel
practice_panel = driver.find_element_by_id('examPractice')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(
    practice_panel).click(practice_panel).perform()

# click the button to start the exam simulation
start_exam_button = driver.find_element_by_class_name('btn-primary')
start_exam_button.click()

# select language
select_menu = Select(driver.find_element_by_id('LanguageId'))
select_menu.select_by_value('15')
# send this form
send_language_info = driver.find_element_by_id('btnChooseLanguageNext')
send_language_info.click()

# confirm that you want to start by clicking yes button
# say da to finally start an exam
start_exam_final = driver.find_element_by_id('alertify-ok')
ActionChains(driver).move_to_element(
    start_exam_final).click(start_exam_final).perform()

# time.sleep(5)
# driver.quit()

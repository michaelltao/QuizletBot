from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
start_time = time.time()
options = Options()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome('/Users/michaeltao/Downloads/chromedriver')
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)
# driver.get('https://10minutemail.net/')
# driver.find_element(By.ID, 'copy-button').click()
driver.get('https://tempmailo.com/')
driver.find_element(By.CLASS_NAME, 'iconx').click()

driver.get('https://quizlet.com/')

driver.find_element(By.CSS_SELECTOR, "[aria-label='Sign up']").click()
driver.find_element(By.CSS_SELECTOR, "[aria-label='birth_month']").send_keys('j')
driver.find_element(By.CSS_SELECTOR, "[aria-label='birth_day']").send_keys('1')
driver.find_element(By.CSS_SELECTOR, "[aria-label='birth_year']").send_keys('1')
driver.find_element(By.ID, 'email').send_keys(Keys.COMMAND, 'v')
driver.find_element(By.ID, 'password1').send_keys('bigcockman')
driver.find_element(By.ID, 'password1').submit()
# driver.find_element(By.CSS_SELECTOR, "[aria-label='Continue to free Quizlet']").click()
print(time.time() - start_time)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/vsawant/PycharmProjects/drivers/chromedriver/chromedriver")

driver.implicitly_wait(1)
driver.get("https://www.google.com")
print(driver.title)

ele = driver.find_element_by_name("q").send_keys("naveen automationlabs")

options = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print("No of options : ", len(options))
for option in options:
    print(option.text)

time.sleep(1)
driver.close()
driver.quit()

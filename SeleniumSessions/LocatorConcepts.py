from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "chromium"
driver = None

if browserName == "chromium":
    # Automatically download and install chromium executable
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

elif browserName == "chrome":
    # Automatically download and install chrome executable
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browserName == "firefox":
    # GeckoDriverManager will give the path to download and install firefox driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:
    print("Please pass the correct browser name : " + browserName)
    raise Exception("Driver is not found")

driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print("Page Title : ",driver.title)

URL_text_field = driver.find_element(By.ID, "Form_submitForm_subdomain")
URL_text_field.send_keys("Naveen automation labs")

# Find element with the help of ID
firstname = driver.find_element(By.ID, "Form_submitForm_FirstName")
lastname = driver.find_element(By.ID, "Form_submitForm_LastName")
# Find element with the help of NAME
email = driver.find_element(By.NAME, "Email")
job_title = driver.find_element(By.NAME, "JobTitle")
# Find element with the help of XPATH
company_name = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_CompanyName']")
# Find element with the help of LINK TEXT
feature_link = driver.find_element(By.LINK_TEXT, "Features")

# Find element from drop down list
# 1 By index
ele_num_of_emp_drop_down = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
element_emp = Select(ele_num_of_emp_drop_down)
element_emp.select_by_index(2)
time.sleep(2)
# 2 By text
ele_industry_drop_down = driver.find_element(By.ID, "Form_submitForm_Industry")
element_ind = Select(ele_industry_drop_down)
element_ind.select_by_visible_text("Automotive")
time.sleep(2)
# 3 By value
ele_country_drop_down = driver.find_element(By.ID, "Form_submitForm_Country")
element_country = Select(ele_country_drop_down)
element_country.select_by_value("India")
time.sleep(2)

firstname.send_keys("Vijay")
lastname.send_keys("Sawant")
email.send_keys("vijaysawant@gmail.com")
job_title.send_keys("Software Engineer")
company_name.send_keys("ABC Private limited")
feature_link.click()

time.sleep(2)
driver.quit()
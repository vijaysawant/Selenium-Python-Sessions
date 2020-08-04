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

elif browserName == "firefox":
    # GeckoDriverManager will give the path to download and install firefox driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:
    print("Please pass the correct browser name : " + browserName)
    raise Exception("Driver is not found")

driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print("Page Title : ",driver.title)
# import pdb; pdb.set_trace()
### with the help of select class ###
drop_down_ele_num_of_emp = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
select = Select(drop_down_ele_num_of_emp)
num_of_emp_list = select.options
# Printing available options from drop down list (Number of employees)
for element in num_of_emp_list:
    print(element.text)

### without help of select class ###
# select country from available options from drop down list (country)
num_of_emp_list_1 = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Country']/option")
for ele in num_of_emp_list_1:
    if(ele.text == "India"):
        ele.click()
        print("Selected country name -> India")
        break

time.sleep(2)
driver.quit()
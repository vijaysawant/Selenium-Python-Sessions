from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
import time

def select_value_from_drop_down(select_by=None, web_element=None, value=None):
    if select_by is None:
        raise Exception("Please specify proper input method")
    if web_element is None:
        raise Exception("Please pass proper web element")
    if value is None:
        raise Exception("Please provide value to select")

    select = Select(web_element)
    if select_by == "index":
        select.select_by_index(value)
    elif select_by == "text":
        select.select_by_visible_text(value)
    elif select_by == "value":
        select.select_by_value(value)
    else:
        raise Exception ("Passed wrong select option")
    return (select.first_selected_option).text

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

# 1 By index
ele_num_of_emp = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
retVal = select_value_from_drop_down(select_by="index", web_element=ele_num_of_emp, value=2)
print("Number of emp : ", retVal)

# 2 By visible text
ele_industry = driver.find_element(By.ID, "Form_submitForm_Industry")
retVal = select_value_from_drop_down(select_by="text", web_element=ele_industry, value="Automotive")
print("Industry is : ", retVal)

# 3 By value
ele_country = driver.find_element(By.ID, "Form_submitForm_Country")
retVal = select_value_from_drop_down(select_by="value", web_element=ele_country, value="India")
print("Country Name : ", retVal)

time.sleep(2)
driver.quit()
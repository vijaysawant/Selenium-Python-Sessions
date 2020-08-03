from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import yaml
import time

config_Val = yaml.load(open("../conf.yaml"), Loader=yaml.FullLoader)

browserName = "chromium"
driver = None
#
chrome_options = Options()
chrome_options.add_argument("ignore-certificate-errors")

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

if browserName == "chromium":
    # Automatically download and install chromium executable
    print("Login via chromium browser")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)

elif browserName == "chrome":
    # Automatically download and install chrome executable
    print("Login via chrome browser")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

elif browserName == "firefox":

    # GeckoDriverManager will give the path to download and install firefox driver
    print("Login via firefox browser")
    # driver = webdriver.Firefox(capabilities=cap, executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
else:
    print("Please pass the correct browser name : " + browserName)
    raise Exception("Driver is not found")

base_URL = config_Val["base_URL"]
driver.implicitly_wait(5)
driver.get(base_URL)

#Enter the username
Login_txt = driver.find_element(By.NAME, "login[login]")
Login_txt.clear()
Login_txt.send_keys(config_Val["username"])

#Enter the password
Passwd_txt = driver.find_element(By.NAME, "login[password]")
Passwd_txt.clear()
Passwd_txt.send_keys(config_Val["password"])

#Click on login btn
Login_btn = driver.find_element(By.NAME, "commit")
Login_btn.click()
print("Login successful..!")

#Is login successful
Brand_name = driver.find_element(By.CLASS_NAME, "navbar-brand-txt")
if Brand_name.is_displayed():
    Brand_name.click()
else:
    print("Page not loaded correctly")
# import pdb;
try:
    href_list = []
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        # print("Text : ",link.text)
        href = link.get_attribute("href")
        if (href not in href_list) and (href != base_URL + "#"):
            href_list.append(href)
            print("\thref attr : ",href)
    # print("----------------", len(href_list))

    for link in href_list:
        driver.get(link)
        time.sleep(1)
        print(driver.title)
except Exception as e:
    print("Exception found : ",e)
Acc_menu = driver.find_element(By.ID, "account_menu")
Acc_menu.click()
driver.implicitly_wait(1)
Logout_btn = driver.find_element(By.XPATH, "//*[contains(@href, '/users/logout') and contains(text(), 'Log Out')]")
Logout_btn.click()
print("Logout successful..!")


time.sleep(2)
driver.quit()
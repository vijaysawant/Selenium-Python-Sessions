from selenium import webdriver
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "firefox"
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
driver.get("https://www.google.com/")

driver.quit()

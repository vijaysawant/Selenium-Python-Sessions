from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import yaml
import time

config_Val = yaml.load(open("../conf.yaml"), Loader=yaml.FullLoader)
browserName = "chrome"
driver = None
chrome_options = Options()
chrome_options.add_argument("ignore-certificate-errors")

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

if browserName == "chromium":
    # Automatically download and install chromium executable
    print("Login via chromium browser")
    # driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
    driver = webdriver.Chrome("/home/vsawant/.wdm/drivers/chromedriver/linux64/86.0.4240.22/chromedriver")

elif browserName == "chrome":
    # Automatically download and install chrome executable
    print("Login via chrome browser")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver = webdriver.Chrome("../web-drivers/chromedriver-86.0.4240.22/chromedriver", options=chrome_options)
elif browserName == "firefox":

    # GeckoDriverManager will give the path to download and install firefox driver
    print("Login via firefox browser")
    # driver = webdriver.Firefox(capabilities=cap, executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
    driver = webdriver.Firefox(executable_path="/home/vsawant/PycharmProjects/Selenium-Python-Sessions/web-drivers/geckodriver-v0.28.0/geckodriver")

else:
    print("Please pass the correct browser name : " + browserName)
    raise Exception("Driver is not found")

base_URL = config_Val["base_URL"]
driver.implicitly_wait(5)
driver.get(base_URL)
driver.maximize_window()
# print(driver.get_window_size())
# {'width': 1920, 'height': 1053}

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
time.sleep(2)
Brand_name = driver.find_element(By.CLASS_NAME, "navbar-brand-txt")
if Brand_name.is_displayed():
    Brand_name.click()
else:
    print("Page not loaded correctly")
# import pdb;
def get_header_text(webdriver = None):
    try:
        tag = webdriver.find_element(By.TAG_NAME, "H1")
        if tag.is_displayed():
            return True, str(tag.text)
    except Exception as e:
        print("Exception occures : ",e)
        return False, None

try:
    href_list = []
    pages_visited = []
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        # print("Text : ",link.text)
        href = link.get_attribute("href")
        if (href not in href_list) and (href != base_URL + "#"):
            href_list.append(href)
            # print("\thref attr : ",href)
    import pdb;
    Link_number = 1
    i = 1
    for link in href_list:
        print(f"Link {Link_number} = ", link)
        driver.get(link)
        Link_number = Link_number + 1
        time.sleep(1)
        # pdb.set_trace()
        # ret_val, header_text = get_header_text(webdriver=driver)
        # ret_val = True    ### dummy ###
        # if ret_val is False:
        #     print("Looking for tag <H2>")
        #     tag = driver.find_element(By.TAG_NAME, "H2")
        #     header_text = "Random_text_" + Link_number
        if driver.title != "":
            # pdb.set_trace()
            header_text = driver.title  ### dummy ###
            if header_text not in pages_visited:
                pages_visited.append(header_text)
                # print(tag.text)
                # File Name and File Path defines here.
                file_name = f"{i}_{header_text}.png"
                file_path = "/home/vsawant/PycharmProjects/Selenium-Python-Sessions/screen_shots/" + file_name
                # Taking screen shot here.
                driver.get_screenshot_as_file(filename=file_path)
                # if i == 2:
                #     break
                i = i+1
        else:
            continue
except Exception as e:
    print("Exception found : ",e)
time.sleep(2)
driver.get(base_URL)
Acc_menu = driver.find_element(By.ID, "account_menu")
Acc_menu.click()
driver.implicitly_wait(1)
Logout_btn = driver.find_element(By.XPATH, "//*[contains(@href, '/users/logout') and contains(text(), 'Log Out')]")
Logout_btn.click()
print("Logout successful..!")


time.sleep(2)
driver.quit()
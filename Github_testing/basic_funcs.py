import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from browser_config import get_options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

options = get_options()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://github.com/")

cookies = pickle.load(open("github_cookies.pkl", "rb"))
for c in cookies:
    try:
        driver.add_cookie(c)
    except:
        pass

driver.get("https://github.com/")

if "Sign in" in driver.page_source:
    print("Session expired.")
else:
    print("Logged in using cookies.")

wait = WebDriverWait(driver, 10)

#minimise window
driver.minimize_window()
time.sleep(1)

# Restore window
driver.maximize_window()
time.sleep(1)

# Refresh the page
driver.refresh()
time.sleep(1)

# Back
driver.back()
time.sleep(2)

# Forward
driver.forward()
time.sleep(2)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Scroll up
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# Close the browser
driver.quit()

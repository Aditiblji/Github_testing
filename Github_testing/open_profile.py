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

#Click on avatar and profile
elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Open user navigation menu']")
print("Count:", len(elements))
for e in elements:
    print(e.size, e.is_displayed(), e.is_enabled())
profile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open user navigation menu']"))
)

try:
    profile.click()
except:
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

time.sleep(3)
profile1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id=':r15:--label']"))
)
try:
    profile1.click()
except:
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

time.sleep(3)
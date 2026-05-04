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

#search for an account
try:
    # GitHub universal hotkey to open search box
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys("/")
    time.sleep(2)

    # After pressing "/", GitHub opens the real search input.
    search_input = wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            "input.header-search-input, input#query-builder-test, input[data-hotkey='s, /']"
        ))
    )
    print("Search input opened via hotkey.")

except TimeoutException:
    raise Exception("GitHub search box refused to open. They changed something again.")
time.sleep(3)
# Enter text
search_input.clear()
search_input.send_keys("Aditiblji")
time.sleep(2)
search_input.send_keys(Keys.ENTER)
print("Search text entered.")
time.sleep(3)
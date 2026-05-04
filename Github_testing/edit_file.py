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

# Click on Avatar -> Profile
time.sleep(3)
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
    time.sleep(5)

profile1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id=':r19:--label']"))
)
try:
    profile1.click()
except:
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(5)

# Click on the repository
repo_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-repositories-list"))
)

# this selects actual repository list items
repos = repo_list.find_elements(By.CSS_SELECTOR, "li.source")

if repos:
    first_repo = repos[0]
    link = first_repo.find_element(By.TAG_NAME, "a")
    link.click()

time.sleep(5)
# To click on edit button of Readme.md
edit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Edit file']"))
).click()

time.sleep(3)
content = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
)
content.click()
# cursor to last line
content.send_keys(Keys.CONTROL, Keys.END)

content.send_keys("Successfully typed in the file!!")
time.sleep(3)
content.send_keys("Content to erase")
time.sleep(3)
# Crtl+Z
content.send_keys(Keys.CONTROL, 'z')
time.sleep(3)
# commit changes
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Commit changes...')]"))
).click()
time.sleep(3)
# Commit changes confirm
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[@class='prc-Button-Label-pTQ3x'][normalize-space()='Commit changes']"))
).click()

time.sleep(5)

driver.quit()




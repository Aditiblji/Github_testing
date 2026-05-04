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

# click the branch dropdown
branch_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#ref-picker-repos-header-ref-selector"))
)
branch_dropdown.click()
time.sleep(3)

# click "View all branches"
view_all = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".RefSelectorV1-module__ViewAllRefsActionText--T80I4"))
)
view_all.click()

time.sleep(3)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//body[1]/div[1]/div[6]/div[1]/main[1]/turbo-frame[1]/div[1]/react-app[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/div[1]/button[1]"))
).click()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()



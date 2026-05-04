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

#directly go to repo

driver.get("https://github.com/CU22BCA005A/test/")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,"pull-requests-tab"))
).click()
time.sleep(3)

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".Button--primary.Button--medium.Button"))
).click()

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"details[id='base-ref-selector'] summary[class='branch Button--secondary Button--small Button']"))
).click()
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > main:nth-child(1) > turbo-frame:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > details:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input-demux:nth-child(2) > tab-container:nth-child(2) > div:nth-child(2) > ref-selector:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(2)"))
).click()
time.sleep(3)
driver.refresh()
time.sleep(3)
WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Create pull request')]"))
).click()
time.sleep(3)
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='pull_request_title']"))
).send_keys("Want to contribute!")

time.sleep(3)

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']//span[contains(text(),'Create pull request')]"))
).click()

time.sleep(15)

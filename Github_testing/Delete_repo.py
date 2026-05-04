# main_script.py
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from login_func import github_login  # import the function
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from browser_config import get_options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Use the login function
github_login(
    driver,
    username="<github_emailID>",
    password="<github_password>"
)

driver.get("https://github.com/CU22BCA005A/Selenium")
settings = driver.find_element(By.CSS_SELECTOR, "span[data-content='Settings']").click()
delete_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='dialog-show-repo-delete-menu-dialog']"))
)
delete_btn.click()

confirm_delete = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='repo-delete-proceed-button']"))
)
confirm_delete.click()
submit_delete = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'I have read and understand these effects')]"))
)
submit_delete.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@id='verification_field']"))
).send_keys("CU22BCA005A/Selenium")

WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[@id='repo-delete-proceed-button']//span[@class='Button-label'][normalize-space()='Delete this repository']"))
).click()
time.sleep(3)
driver.quit()

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
    username="aditib.bca22@chanakyauniversity.edu.in",
    password="Microsoft.k@.baccha1"
)

# Now you're logged in, continue with your upload etc.
driver.get("https://github.com/CU22BCA005A/Selenium/upload/main")

# upload input
upload_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "upload-manifest-files-input"))
)
upload_input.send_keys(r"D:\CU Journey\Semesters\7th Semester\Software testing\Agile_testing.pdf")

# Fill out details
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "commit-summary-input"))
).send_keys("Topic")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "commit-description-textarea"))
).send_keys("Desc...")

time.sleep(10)

commit = driver.find_element(By.CSS_SELECTOR,".js-blob-submit.btn-primary.btn").click()


time.sleep(10)

driver.quit()
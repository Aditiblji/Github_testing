import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_config import get_options

options = get_options()
driver = webdriver.Chrome(options=options)

driver.get("https://github.com/login")

login_id = driver.find_element(By.ID, "login_field")
login_id.send_keys("<github_emailID>")

login_p = driver.find_element(By.ID, "password")
login_p.send_keys("<github_password>")

btn = driver.find_element(By.NAME, "commit")
btn.click()

btn1 = WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-webauthn-confirm-button"))
)
btn1.click()

# wait for login cookie
WebDriverWait(driver, 30).until(
    lambda d: d.get_cookie("logged_in") and d.get_cookie("logged_in")["value"] == "yes"
)

pickle.dump(driver.get_cookies(), open("github_cookies.pkl", "wb"))
print("cookies saved")
driver.quit()

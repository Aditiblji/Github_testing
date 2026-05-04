# github_login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def github_login(driver, username, password, timeout=120):
    driver.get("https://github.com/login")

    # Enter username
    login_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )
    login_id.send_keys(username)

    # Enter password
    login_p = driver.find_element(By.ID, "password")
    login_p.send_keys(password)

    # Login submit
    btn = driver.find_element(By.NAME, "commit")
    btn.click()

    # Handle WebAuthn / security key approval
    try:
        btn1 = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-webauthn-confirm-button"))
        )
        btn1.click()
    except:
        pass  # no 2FA prompt shown

    # Wait until logged_in cookie becomes yes
    WebDriverWait(driver, 30).until(
        lambda d: d.get_cookie("logged_in") and d.get_cookie("logged_in")["value"] == "yes"
    )

    return True

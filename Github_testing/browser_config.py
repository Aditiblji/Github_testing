from selenium import webdriver

def get_options():
    options = webdriver.ChromeOptions()

    # Add whatever options you usually use
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # If you want headless mode uncomment:
    # options.add_argument("--headless=new")

    return options

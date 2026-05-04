# Github_testing

This repository contains a collection of Python scripts designed to automate and test various workflows on GitHub using Selenium WebDriver.

## 🚀 Overview

The project simulates real user interactions with GitHub, including:

* Logging in using saved session cookies
* Navigating user profiles
* Accessing repositories
* Managing branches
* Performing repository actions (create, delete, edit, etc.)

It is intended for learning, experimentation, and automation testing purposes.

## ⚙️ Requirements

* Python 3.x
* Google Chrome
* ChromeDriver (compatible with your Chrome version)
* Selenium

Install dependencies:

```bash
pip install selenium
```

## 🔐 Authentication

This project uses stored cookies (`github_cookies.pkl`) to bypass manual login.

To generate cookies:

1. Log in to GitHub manually using Selenium or browser.
2. Save session cookies using `pickle`.
3. Store them in `github_cookies.pkl`.

⚠️ Keep this file secure. It contains your authenticated session data.

## 🧪 Sample Workflow

The provided scripts can:

1. Open GitHub
2. Inject saved cookies
3. Verify login session
4. Navigate to user profile
5. Open a repository
6. Interact with branches (view, switch, etc.)

## ▶️ Running a Script

```bash
python your_script_name.py
```

Example:

```bash
python open_profile.py
```

## 🧠 Key Features

* Automated login via cookies
* Explicit waits for stable element interaction
* Modular scripts for different GitHub actions
* Error handling for dynamic UI elements

## ⚠️ Notes

* GitHub UI changes frequently, which may break selectors.
* Some selectors (like dynamic IDs) may need updating.
* Avoid excessive automation to prevent account restrictions.

## 📌 Disclaimer

This project is for educational and testing purposes only. Use responsibly and ensure compliance with GitHub’s terms of service.

---


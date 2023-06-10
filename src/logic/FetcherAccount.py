from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FetcherAccount:
    chrome_driver_path:str
    chrome_options:Options
    driver:webdriver.Chrome
    email:str
    password:str
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.webdriver_path = "assets/drivers/chromedriver"  # Replace with the actual path
        self.driver = webdriver.Chrome(executable_path=self.webdriver_path, options=self.chrome_options)
        self.email = "bombkiller36@gmail.com"
        self.password = "BOmB123456789"

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email_input.send_keys(self.email)  # Replace with your email address

        # Find the password input field and enter your password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(self.password)  # Replace with your password

        # Find and click the "Sign in" button
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        sign_in_button.click()

        # Wait for the login process to complete and wait for the dashboard page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "ember8"))
        )

    def get_html(self, link:str) -> str:
        self.driver.get(link)
        return self.driver.page_source

    def logout(self):
        self.driver.close()
        


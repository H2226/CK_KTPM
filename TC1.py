import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin:
    def setup_method(self, method):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://viblo.asia/") 

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        time.sleep(3)
        click_btn_logIn = self.driver.find_element(By.CLASS_NAME, "login-button")
        click_btn_logIn.click()
        def click_login():
            login_button = self.driver.find_element(By.XPATH, "//button[@class='el-button w-100 el-button--primary']")
            login_button.click()
        try:
            info = self.driver.find_elements(By.CLASS_NAME, "el-input__inner")
            username = info[0]
            password = info[1]
            username.clear()
            password.clear()

            username.send_keys("QH281202")
            password.send_keys("qGV3Q5JQxEMN*Bf")
            click_login()
            time.sleep(5)
            if "Wrong username/email or password" in self.driver.page_source:
                print("Test passed: Incorrect credentials message displayed")
            else:
                print("Test failed: No error message displayed")
        except Exception as e:
            print(e)
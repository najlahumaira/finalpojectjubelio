import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

class TestLogin(unittest.TestCase):
    def test_a_success_login(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://app.jubelio.com/login")

        self.driver.find_element(By.NAME,"email").send_keys("qa.rakamin.jubelio@gmail.com")
        self.driver.find_element(By.NAME,"password").send_keys("Jubelio123!")
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "ladda-button").click()
        time.sleep(1)
    
                      
        def tearDown(self):
         self.browser.close()


if __name__ == "__main__":
    unittest.main()


      


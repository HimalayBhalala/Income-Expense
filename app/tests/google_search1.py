from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

driver = None

class GoogleSearch(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver =  webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        return driver
    
    def test(self):
        driver.find_element(By.NAME,'q').send_keys('Ratan tata')
        time.sleep(2)
        driver.find_element(By.NAME,'btnK').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,'VuuXrf').click()
        
    def tearDown(self):
        time.sleep(10)  
        driver.close()
        
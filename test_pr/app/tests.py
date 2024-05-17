#####################################

# Test included :
#     test scenario,
#     test case,
#     test suite

# How to perfrom unit testing
    # module name:unittest (inbuild included)
    # classname : TestCase
    # instance method : 3 methods

    # 1.setUp()
    # 2.test()
    # 3.tearDown()

    # (Run like init,service,destroy)

# NOTE : Run every time 1)Setup----test_method1-----tearDown,   2)Setup----test_method2----tearDown

######################################################################################################

# Ex:

#     SetUp(): open chrome
#     test1(): test login functionality using chrome
#     tearDown(): close chrome

#     SetUp(): open FireFox
#     test1(): test login functionality using FireFox
#     tearDown(): close FireFox

    # Make seprate for SetUp() seprate so only one time can run

    # test1: test login functionality in chrome using validpassword and validpassword
    # test2: test login functionality in FireFox using invalidpassword and invalidpassword

    # Make seprate for TearDown() seprate so only one time can run

# Note : 
#     Ex:
#         10 test method
#             Setup() -> 10
#             TearDown() -> 10
#             SetupClass() -> 1
#             Teardownclass() -> 1

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # Manual Testing -> 
    # Authomation Testing -> Selenium,QTP,Load Runner

# Ex:
#     Google Search functionality

#     1.open firefox browser
#     2.open google.com
#     3.click search
#     4.type you whant to search
#     5.click to wikipedia

# import unittest

# class TestCasePractice(unittest.TestCase):
    
#     @classmethod  #run as a fixures
#     def setUpClass(cls):
#         print("Only one setup class method is executed.....")

#     def setUp(self):
#         print("Setup is ready......")

#     def test_method1(self):
#         print("Testing1 is runing")
#         print(1/0)

#     def test_method2(self):
#         print("Testing2 is runing")

#     def test_method3(self):
#         print("Testing3 is runing")
        
#     def tearDown(self):
#         print("Test is teardown")

#     @classmethod
#     def tearDownClass(cls):
#         print("Only one time teardown class method is running")


# google search based functionality 
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

driver = None

class GoogleSearch(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://www.google.com/")
        driver.maximize_window()

    def test(self):
        time.sleep(2)
        driver.find_element(By.NAME, 'q').send_keys('Bill Gates')  # Using find_element with By.NAME for the search input field
        time.sleep(5)  # It's better to use WebDriverWait instead of time.sleep for waiting
        driver.find_element(By.NAME, 'btnK').click()  # Assuming the name of the search button is 'btnK'
        time.sleep(5)

    def tearDown(self) -> None:
        time.sleep(10)  # Consider using WebDriverWait instead of time.sleep
        driver.close()

########################################### Testing login and logout functionality ###################################

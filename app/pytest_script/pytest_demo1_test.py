# yield is working is a generator it containes lisr of item or tuple

# import pytest

# @pytest.fixture(scope='module')
# def setteardownClass():
#     print("SetUp is working .................")
#     yield
#     print("TearDown is working..............")

# @pytest.fixture()
# def setteardownmethod():
#     print("setup")
#     yield
#     print("teardown")

# def test_demo1(setteardownClass,setteardownmethod):
#     print("Test_demo1 is running currently")

# def test_demo2(setteardownClass,setteardownmethod):
#     print("Test_demo2 is running currectly")


# from .common_test import SetUpTearDownClass,setupmethod
# import pytest

# @pytest.mark.run(order=2)
# def test_methodC():
#     print("test_method c is executed")

# @pytest.mark.run(order=3)
# def test_methodA():
#     print("test_method a is executed")

# @pytest.mark.run(order=1)
# def test_methodB():
#     print("test method b is executed")


# from .common_test import SetUpTearDownClass,setupmethod
# import pytest

# @pytest.mark.run(order=-2)
# def test_methodC():
#     print("test_method c is executed")

# @pytest.mark.run(order=-3)
# def test_methodA():
#     print("test_method a is executed")

# @pytest.mark.run(order=-1)
# def test_methodB():
#     print("test method b is executed")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = None

# class TestGoogleSearch():
#     @pytest.fixture()
#     def setUpTearDown(self):
#         global driver
#         driver = webdriver.Chrome()
#         driver.get('https://www.google.com')
#         driver.maximize_window()
#         yield
#         time.sleep(20)
#         driver.close()

#     def test_googleFunctionalit(self,setUpTearDown):
#         time.sleep(1)
#         driver.find_element(By.NAME,'q').send_keys("Steve Jobs")
#         time.sleep(2)
#         driver.find_element(By.NAME,'btnK').click()
#         time.sleep(1)
#         driver.find_element(By.CLASS_NAME,'VuuXrf').click()

# class TestLoginAndLogout():
#     @pytest.fixture(scope='module')
#     def setUpTearDown(self):
#         global driver
#         driver = webdriver.Chrome()
#         time.sleep(1)
#         driver.get('http://localhost:8000/api/')
#         driver.maximize_window()
#         yield
#         time.sleep(10)
#         driver.close()

#     @pytest.mark.run(order=2)
#     def test_logout(self,setUpTearDown):
#         driver.find_element(By.LINK_TEXT,'Logout').click()
#         time.sleep(2)
#         driver.find_element(By.NAME,'signout').click()
#         time.sleep(2)

#     @pytest.mark.run(order=1)
#     def test_login(self,setUpTearDown):
#         time.sleep(1)
#         driver.find_element(By.LINK_TEXT,'Login').click()
#         time.sleep(2)
#         driver.find_element(By.NAME,'login').send_keys("admin")
#         driver.find_element(By.NAME,'password').send_keys("admin")
#         time.sleep(3)
#         driver.find_element(By.NAME,'remember').click()
#         time.sleep(1)
#         driver.find_element(By.NAME,'signin').click()
#         time.sleep(3)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None

class TestApi():
    @pytest.fixture()
    def setUpAndTearDown(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        driver.maximize_window()
        yield
        time.sleep(10)
        driver.close()

    def test_A(self,setUpAndTearDown):
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,'opblock opblock-post is-open').click()

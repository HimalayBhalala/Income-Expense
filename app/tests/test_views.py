#####################################

# unit testing is used for reducing bug

# Test included :
#     test scenario,
#     test case,
#     test suite


# NOTE: test suite means a goup of testcases

# How to perfrom unit testing
    # module name:unittest (inbuild included)
    # classname : TestCase
    # instance method : 3 methods

    # 1.setUp()
    # 2.test()
    # 3.tearDown()

    # (Run like init,service,destroy)

# class TestView(TestCase):
#     def test_user_can_not_authenticated_with_data(self):
#         response = self.client.post(self.register_url)
#         # import pdb
#         # pdb.set_trace()
#         self.assertEqual(response.status_code,400)

#     def test_user_can_access_data(self):
#         response = self.client.post(self.register_url,self.user_data,format='json')
#         # import pdb
#         # pdb.set_trace()
#         self.assertEqual(response.data['email'],self.user_data['email'])
#         self.assertEqual(response.data['username'],self.user_data['username'])
#         self.assertEqual(response.status_code,201)

#     def test_user_cannot_login_with_unverified_email(self):
#         response = self.client.post(self.login_url,self.user_data,format='json')
#         # import pdb
#         # pdb.set_trace()
#         self.assertEqual(response.status_code,401)

#     def test_user_can_login_after_verification(self):
#         response = self.client.post(self.register_url,self.user_data,format='json')
#         # import pdb
#         # pdb.set_trace()
#         email = response.data['email']
#         user = User.objects.get(email=email)
#         user.is_verified = True
#         user.save()
#         resp = self.client.post(self.login_url,self.user_data,format='json')
#         self.assertEqual(resp.status_code,202)

##################### Test Login View Using salanium ###########################

# SALENIUM =>  Functional testing automation

# from .test_setup import TestSetUp,driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class LoginTest(TestSetUp):
#     def test1(self):
#         import pdb
#         pdb.set_trace()
#         driver.find_elements(By.NAME,'opblock opblock-post is-open').click()


############################### SELENIUM ###################################
# first : pip install selenium
# webdrive(User or client) : use for automation testing.
# webdrive module contains classes and function for testing.

# _________________________________________________
# First launce web browser.

# Browser driver must be required for launch browser
# website for salenium is saleniumhq.org

######################## Example #######################
# import time

# from selenium import webdriver

# driver = webdriver.Chrome()

# driver.get('https://www.google.com')

# driver.maximize_window()

# print("TITLE",driver.title)

# print("Current Page URL",driver.current_url)

# time.sleep(5)

# driver.get('http://localhost:8000')

# print("TITLE",driver.title)

# print("Current Page URL",driver.current_url)

# time.sleep(5)

# driver.back()
# print("After back Current url: ",driver.current_url)

# time.sleep(2)

# driver.forward()
# print("Driver forward url is: ",driver.current_url)

# time.sleep(2)

# driver.close()

#1) driver.get('www.google.com')  #=> get(url)
#2) driver.maximize_window() #=> maximize for testing safe



#3) driver.title()
#4) driver.current_url()
#5) driver.refresh()
#     driver.get(driver.current_url)

# 6) driver.back() => go one step backword in browser history
# 7) driver.forwad() => go one step forward in browser history

# 8) driver.close() => close current window

# 9) driver.quit() => close associalted window also


 
############### How to locate web element #############

# import time
# 
# from selenium import webdriver
# 
# from selenium.webdriver.common.by import By
# 
# driver = webdriver.Chrome()

# driver.find_element(By.ID,'id')
# driver.find_element(By.NAME,'name')
# driver.find_element(By.CLASS_NAME,'class name')
# driver.find_element(By.LINK_TEXT,'link_text')
# etc

# from selenium import webdriver
# import unittest
# import time
# from selenium.webdriver.common.by import By

# driver = None

# class GoogleSearch(unittest.TestCase):
    
#     def setUp(self):
#         global driver
#         driver =  webdriver.Chrome()
#         driver.get('https://www.google.com')
#         driver.maximize_window()
#         return driver
    
#     def test(self):
#         driver.find_element(By.NAME,'q').send_keys('Ratan tata')
#         time.sleep(2)
#         driver.find_element(By.NAME,'btnK').click()
        
#     def tearDown(self):
#         time.sleep(100)  
#         driver.close()
        

##################### unit test ####################

# module : unittest
# class_name : TestCase

# instance method():
#     1) setUp()
#     2) testMethod()
#     3) tearDown()

# class Method():
#     1) setUpClass()
#     2) tearDownclass()

#NOTE: Unittest method is executed alphabetical or numerical order.

########### Limitation of unit testing ##############

# import unittest

# class PythonTestCase(unittest.TestCase):
#     def test_2(self):
#         print("test_2 is executed")

#     def test_1(self):
#         print("test_1 is executed")

# if __name__ == '__main__':
#     unittest.main()

# 2) Test result will be displayed to the console only and it is not possible to generate report

# 3) Unitest framework always run using alphabetical order or numerical order not execute customization

# 4) As the part of batch execution(Test suite),all the test method is executed not specify perticular order will be executed

# 5) unitesting only limited setUp() and tearDown() method is there

    # setUpClass() --> Before executing all test method of a testcase class
    # tearDownclass() --> After excuting all test method of a testcase class
    # setUp() --> Before executing every test method
    # tearDown() --> after executing every test method

    # if we want to perform before and after testsuite , unittest framework does not define any methods.


# TEST_SUITES:
# a group of test case class


#$$$$$$$$$$$$$$$$$$$$$$$$$$$ PyTest $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#NOTE:  pytest is a advance version of unittest

# package : pip install pytest(third party framework)

#$$$$$$$$$$$$$$ PyTest naming Rules $$$$$$$$$$$$$$$$$

# 1) File name must be start or ends with 'test'  
    # Ex. 1) test_google_search.py 2) google_search_test.py    

# 2) Class Name must be start with 'Test' 
    # Ex . TestGoogleSearch,TestDemo

#) test method name must be start with 'test_'
    # Ex. test_methd1(),test_method2()

# -s Only print statement is excuted
# -v only passed and failed status is get
# -s -v both are get combined

#$$$$$$$$$$$$$$$$$$ Implement setUp(),tearDown(),setUpClass() and tearDownClass() $$$$$$$$$$$$$$$$$$$$$$$

# implement setUp() method
# _______________________________________________________

    # By using some decorator
    # @pytest.fixure()

    # Ex:

# import pytest
# @pytest.fixture()  ==> meant for setUp mechanism
# def setUp():
#     print("This is a setup method")

# def test_A(setUp):
#     print("This is a test_a method")

# implement tearDown() method

    # Ex.

# import pytest
# @pytest.yield_fixture() ==> meant for both setUp and tearDown
# def setuptearDown():
#     print("set up and Tear Down is working")
 

# implement setupclass() and tearDownClass()
    # Ex.

# import pytest
# @pytest.yield_fixture(scope='module') ==> meant for both setUp and tearDown
# def setUpTearDownclass():
    # print("setup")
    # yield
    # print("teardown")

#$$$$$$$$$$$$$$$$$$$$$$$ Pytest setup,teardown,Setupclass and teardownclass $$$$$$$$$$$$$$$$$$$$$$$$$$

# @pytest.fixures() => used for only setup and combined both using this decorator like setUp and tearDown
# @pytest.fixures(scope='module') => used for getting one time Setup and tearDown class


 #$$$$$$$$$$$$$$$$$$$$$$$$ Possible ways to run pytest $$$$$$$$$$$$$$$$$$$$$$$$$$
# 1) py.test -v -s:
#     to run all test script which have present in current directory

# 2) py.test -v -s test.py:
#     to run all test script of perticular file

# 3) py.test -v -s test.py test1.py:
#     to run multiple test scripts

# 4) py.test -v -s test.py::test_methodB:
#     to run a perticular method in a class

#$$$$$$$$$$$$$$$$$$$ Customize order of tests in pytest $$$$$$$$$$$$$$$$$$$$$

# module => pytest-ordering

# @pytest.mark.run(order=n) where n = 1,2,3,4 ....... n 

#$$$$$$$$$$$$$$$$$$$$$ Generate test result using html form $$$$$$$$$$$$$$$$$
# module name is pytest-html

    # Ex.
    #     pytest -v -s test.py --html=result2.html


#$$$$$$$$$$$$$$$$$$$$$$$$$ All Testing $$$$$$$$$$$$$$$$$$$$$$

#1) unittesting
    # setUp()
    # test_method()
    # teardown()
    # setUpClass()
    # tearDownClass()

#2) pytest
    # @pytest.fixure() => write only setup method
    # @pytest.fixure() => write both setup and teardown method using yield keyword
    # @pytest.fixure(scope='module') => write setUpClass and tearDownClass


#$$$$$$$$$$$$$$$$$$$$$$$$$$$ Django application testing $$$$$$$$$$$$$$$$$$$$$

# Django provide inbuilt test framework(django.test),which is based on unittest framework.
# here TestCaseDemo is a child class of unittest.TestCase

# from django.test import TestCase
# import unittest
# class TestCaseDemo(unittest.TestCase)
    # pass

#$$$$$$$$$$$$$$$$$$$$$$$$$ DRF Application $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# DRF ==> Django Rest Framework

# from rest_framework.test import APITestCase

# NOTE: If api folder is outside of manage.py so simply run 
# command:

#     Ex:
#         python3 manage.py test api_folder_name.tests
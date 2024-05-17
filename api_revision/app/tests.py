from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import ProductSerializer
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.

class TestProductModelCase(TestCase):
    @classmethod
    def setUpClass(self):
        self.model = Product
        self.user = User.objects.create(username='avinash',password='admin')
        self.data = Product.objects.create(name="Kiwi",saler=self.user,price=100)

    def test_hello(self):
        self.assertEqual(1,1)
        self.assertEqual(self.model.__name__,'Product')
        self.assertEqual(self.model.__class__.__name__,'ModelBase')

    def test_check_serializer_is_valid(self):
        data = {"name":"Apple","saler":self.user,"price":400}
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_check_url_data(self):
        url = '/app/product/'
        print(url('http://testserver/schema/'))
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_check_data_created(self):
        url = '/app/product/1/'
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.data['id'],1)

    @classmethod
    def tearDownClass(cls):
        pass


# import time

# driver = None

# class TestProductApi(TestCase):
#     @classmethod
#     def setUpClass(self):
#         global driver
#         driver = webdriver.Chrome()
#         driver.get('http://localhost:8000/app/product/')
#         driver.maximize_window()

#     def test_product_add(self):
#         time.sleep(1)
#         driver.find_element(By.NAME,'name').send_keys("Orange")
#         driver.find_element(By.NAME,'price').send_keys("120")


#     @classmethod
#     def tearDownClass(self):
#         time.sleep(10)
#         driver.close()
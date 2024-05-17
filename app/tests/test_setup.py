# from rest_framework.test import APITestCase
# from django.urls import reverse
# from app.models import User
# from selenium.webdriver.common.by import By
# import time
# from selenium import webdriver


# driver = None
# class TestSetUp(APITestCase):
#     def setUp(self):
#         global driver
#         driver = webdriver.Chrome()
#         driver.get('http://127.0.0.1:8000/')
#         driver.maximize_window()
#         return driver
    
#     def tearDown(self):
#         time.sleep(10)
#         driver.close()

from rest_framework.test import APITestCase,APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import User
from expense.models import Expense
from income.models import Income
import datetime
from django.test import RequestFactory

class TestSetApi(APITestCase):
    @classmethod
    def setUpClass(self):
        self.client = APIClient()
        self.email = 'admin@gmail.com'
        self.password = 'admin'
        self.username = 'admin'
        self.user = User.objects.create_user(email=self.email,username=self.username,password=self.password)
        self.expense_data=None
        self.token = str(RefreshToken.for_user(self.user).access_token)
        Expense.objects.create(owner=self.user,category='Online Service',amount=1000,description="This is a online services")
        Expense.objects.create(owner=self.user,category='Food',amount=200,description="This is a burger food")
        Income.objects.create(owner=self.user,source="Salary",description="This is a based on a total salary",amount=10000,date=datetime.date.today())
        Income.objects.create(owner=self.user,source="Business",description="This is a based on a total money using Bussiness",amount=10000000,date=datetime.date.today())
        self.factory = RequestFactory()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
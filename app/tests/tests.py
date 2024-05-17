# from .testcase1 import *
# from .testcase2 import *
# import unittest

# t1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseExa1)
# t2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseExa2)

# t = unittest.TestSuite([t1,t2])
# unittest.TextTestRunner().run(t)

# from django.test import TestCase
# from django.test.client import RequestFactory
# from app.models import User
# from django.urls import reverse
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# import jwt
# from django.conf import settings
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from app.utils import Util 
# from django.utils.encoding import force_bytes,force_str,smart_str
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
# from django.utils import encoding
# from django.contrib.sites.shortcuts import get_current_site

# class TestFunctionality(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.user = User.objects.create_user(username="mahesh",         password="admin@123",email="mahesh@gmail.com")
#         cls.token = str(RefreshToken.for_user(cls.user).access_token)
#         payload = jwt.decode(cls.token,settings.SECRET_KEY,algorithms=['HS256'])
#         user = User.objects.get(id=payload['user_id'])
#         if not user.is_verified:
#             user.is_verified = True
#             user.save()
#             print("User is verified")
#         cls.uid64 = None
#         cls.token = None

#     def test_login(cls):
#         URL = reverse('login')
#         data = {
#             "email":"mahesh@gmail.com",
#             "password":"admin@123",
#         }
#         res = cls.client.post(URL,data=data)
#         cls.assertEqual(res.status_code,202)

#     def test_password_reset_email(cls,request):
#         email = User.objects.get(email=cls.user)
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             cls.token = PasswordResetTokenGenerator().make_token(user)
#             cls.uid64 = urlsafe_base64_encode(encoding.force_bytes(user.id))
#             print(cls.uid64)
#             relativelink = str(reverse('password-reset-confirm',kwargs={'uid64':cls.uid64,'token':cls.token}))
#             absolute_url = "http://127.0.0.1:8000"+relativelink
            
#             email_body = f"Hello,\n click below Link For reset the password\n"+absolute_url

#             data = {'email_body':email_body,'email_subject':"Password Reset Verify",'to':[email]}

#             Util.send_email(data)

#     def test_password_token_check(cls):
#         user_id  = smart_str(urlsafe_base64_decode(cls.uid64))
#         user = User.objects.get(id=user_id)

#         if not PasswordResetTokenGenerator().check_token(user,cls.token):
#             cls.assertEqual(cls.status_code,404)


#     @classmethod
#     def tearDownClass(cls):
#         pass


# from rest_framework.test import APIRequestFactory

# factory = APIRequestFactory()

# factory.post('/income/',{'owner':'admin','source':'Salary','amount':10000,'description':"This is a bonus salary"},format='json')

# Django 

# from django.test.client import RequestFactory,encode_multipart
# factory = RequestFactory()
# data = {"data":"markanday"}
# content = encode_multipart('BSHSVAIW12343',data)
# content_type = 'multipart/form-data;boundary:BSHSVAIW12343'
# factory.put('path',content,content_type=content_type)

# from rest_framework.test import APIRequestFactory,force_authenticate
# from app.models import User

# factory = APIRequestFactory()

# user = User.objects.get(email='hanuman@gmail.com')
# request = factory.get('http://127.0.0.1:8000/admin/app/user/')
# force_authenticate(request,user=user,token=request.user.auth_token)






# from rest_framework.test import APIClient

# client = APIClient()

# client.login(username='admin',password='admin',email='admin@gmail.com',token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NzUwNTMzLCJpYXQiOjE3MTU3NDY5MzMsImp0aSI6ImVhMzkwZDllM2JmMzRkOWRhM2I4M2Y3NWExMWUwZDU4IiwidXNlcl9pZCI6MX0.JufOfd9EqI-gdi8_AQFyUmnkPv2LrSy2gQqcPQE74yE')


# from rest_framework.test import RequestsClient
# from django.urls import reverse

# client = RequestsClient()

# res = client.get('/income/')

# assert res.status_code == 200

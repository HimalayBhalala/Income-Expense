from rest_framework import status
import time
import unittest
from .models import Income
import json
import datetime
from app.tests.test_setup import TestSetApi

class TestIncomeApi(TestSetApi):

    def test_public_access(self):
        r = self.client.get('http://testserver/income/getdata/')
        self.assertEqual(r.status_code,200)

    def test_post_income_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        data = {
            "source":"Business",
            "amount":"234999",
            "description":"Steel generation bussiness",
            "date":f"{datetime.date.today()}"
        }
        resp = self.client.post('http://127.0.0.1:8000/income/',data=json.dumps(data),content_type='application/json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)

    def test_put_income_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        data = {
            "source":"Salary",
            "amount":"20000",
            "description":"This is a goverment based salary",
            "date":f"{datetime.date.today()}"
        }
        response = self.client.put('http://127.0.0.1:8000/income/1/',data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_delete_income_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.delete('http://127.0.0.1:8000/income/1/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_get_income_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.get('http://127.0.0.1:8000/income/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['count'],2)
        self.assertEqual(response.data['results'][1]['id'],2)

    def test_get_income_unauthenticated(self):
        response = self.client.get('http://127.0.0.1:8000/income/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    @unittest.skip("Because added time.sleep(6)")
    def test_get_token_invalid_or_expired(self):
        time.sleep(6)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        response = self.client.get('http://127:0.0.1:8000/income/')






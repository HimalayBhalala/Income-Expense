from app.tests.test_setup import TestSetApi
from .models import Expense
from rest_framework import status
import json

class TestExpenseAPI(TestSetApi):
    def test_get_expense_unauthenticated(self):
        response = self.client.get('http://127.0.0.1:8000/expense/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_post_expense_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        data = {
            'category':'Online Service',
            'amount':'30000',
            'description':"This is a nice online services"
        }
        response = self.client.post('http://127.0.0.1:8000/expense/',data=json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.expense_data = Expense.objects.all()
        self.assertTrue(Expense.objects.exists())

    def test_get_expense_list_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.get('http://127.0.0.1:8000/expense/1/')
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(Expense.objects.get(id=1))
        self.assertEqual(response.data['category'],'Online Service')
        self.assertEqual(Expense.objects.filter(id=1).count(),1)

    def test_put_expense_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        new_data = {
            "category":"Online Service",
            "amount":'50000',
            "description":"This is provided good service"
        }
        response = self.client.put('http://localhost:8000/expense/1/',data=new_data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_exepense_by_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.delete('http://localhost:8000/expense/1/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_get_expense_list_all(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+self.token)
        response = self.client.get('http://localhost:8000/expense/')
        self.assertEqual(response.data['count'],2)
        self.assertGreaterEqual(response.data['count'],2)
from expense.models import Expense
from app.tests.test_setup import TestSetApi
from app.models import User
from . import views
from django.contrib.auth.models import AnonymousUser

# Create your tests here.

class TestUserstate(TestSetApi):
    def test_get_total_amount(self):
        amount = 0
        data = Expense.objects.all()
        for d in data:
            amount += d.amount
        self.assertEqual(amount,1200.00)
        self.assertGreater(amount,1000)
        self.assertLessEqual(amount,1200)

    def test_between_10_days(self):

        url = "http://localhost:8000/userstate/get-expense-summary/"

        authorization_headers = f'HTTP_AUTHORIZATION: Bearer {self.token}'

        request = views.ExpenseSummaryView.as_view()
        
        request.user = self.user

        view = views.ExpenseSummaryView().as_view()

        res = view(request)



            
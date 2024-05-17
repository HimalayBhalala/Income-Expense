from django.shortcuts import render
from expense.models import Expense
from income.models import Income
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from rest_framework import status

# Create your views here.

class ExpenseSummaryView(APIView):

    def get_total_amount(self,expenses,category):
        amount = 0
        expenses = Expense.objects.filter(category=category)
        for expense in expenses:
            amount += expense.amount
        return {"amount":amount}

    def get_category(self,expense):
        return expense.category
    
    def get(self,request):
        today_date = datetime.date.today()
        ten_days_ago = today_date - datetime.timedelta(days=10)
        expenses = Expense.objects.filter(owner=request.user,date__gte=ten_days_ago,date__lte=today_date)

        categories = list(set(map(self.get_category,expenses)))

        final = {}
        for category in categories:
            for expense in expenses:
                final[category] = self.get_total_amount(expense,category)
        return Response({"category_data":final},status=status.HTTP_200_OK)

class IncomeSummaryView(APIView):

    def get_income_amount(self,income,source):
        incomes = Income.objects.filter(source=source)
        amount = 0
        for income in incomes:
            amount += income.amount
        return {'amount':amount}

    def get_source(self,income):
        return income.source
    
    def get(self,request):
        today_date = datetime.date.today()
        ten_days_ago = today_date - datetime.timedelta(days=10)

        incomes = Income.objects.filter(owner=request.user,date__gte=ten_days_ago,date__lte=today_date)

        sources = list(set(map(self.get_source,incomes)))

        final = {}

        for source in sources:
            for income in incomes:
                final[source] = self.get_income_amount(income,source)
        return Response({"Income_data":final},status=status.HTTP_200_OK)
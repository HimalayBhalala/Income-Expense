from django.urls import path
from . import views

urlpatterns = [
    path('get-expense-summary/',views.ExpenseSummaryView().as_view(),name='get-expense-summary'),
    path('get-income-summary/',views.IncomeSummaryView.as_view(),name='get-income-summary')
]

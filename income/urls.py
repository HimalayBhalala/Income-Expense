from django.urls import path
from . import views

urlpatterns = [
    path('',views.IncomeListCreateView.as_view(),name='income'),
    path('<int:pk>/',views.IncomeRetrieveUpdateDestroyView.as_view(),name='income'),
    path('getdata/',views.GetIncomeView.as_view(),name='getIncome')
]

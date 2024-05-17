from django.urls import path
from . import views

urlpatterns = [
    path('',views.ExpenseListCreateView.as_view(),name='list-create'),
    path('<int:id>/',views.ExpenseRetieveUpdateDestroyView.as_view(),name='re-up-de')
]

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import ExpenseSerializer
from .models import Expense
from .permissions import IoOwner
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ExpenseListCreateView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class ExpenseRetieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated,IoOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
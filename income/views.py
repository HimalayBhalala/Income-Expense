from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import IncomeSerializer
from .models import Income
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IoOwner

# Create your views here.

class GetIncomeView(ListAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [AllowAny]

class IncomeListCreateView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
class IncomeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [IsAuthenticated,IoOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
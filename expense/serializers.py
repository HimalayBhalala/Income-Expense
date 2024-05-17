from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(max_length=100,read_only=True)
    class Meta:
        model = Expense
        fields = ['id','owner','category','amount','description',
                  'date']
        

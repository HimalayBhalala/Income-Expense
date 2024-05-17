from rest_framework import serializers
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(max_length=200,read_only=True)
    class Meta:
        model = Income
        fields = ['id','owner','source','amount','description','date']
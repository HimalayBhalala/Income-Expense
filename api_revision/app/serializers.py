# import yaml
# from rest_framework import serializers

# with open('app.yml','r') as f:
#     data = yaml.safe_load(f)

# serializer_class_fields = {}

# for field_name,field_data in data['ProductSerializer']['fields'].items():
#     field_type = getattr(serializers,field_data['type'].capitalize() + 'Field')
#     serializer_class_fields[field_name] = field_type()

# ProductSerializer = type('ProductSerializer',(serializers.Serializer,),serializer_class_fields)
# print(ProductSerializer)

from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    saler = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


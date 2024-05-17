import yaml
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ProductSerializer,UserSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import Group
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import io
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.metadata import SimpleMetadata

# Create your views here.
class ProductGetCreate(APIView):
    metadata_class = SimpleMetadata()

    def get(self):
        return Response(self.metadata_class)

    def post(self,request,*args,**kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class ProductRetrieveUpdateDelete(APIView):

    def get_object(self,pk):
        try:
            product = Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise Exception("No data")
        
    def get(self,request,pk,*args,**kwargs):
        product = Product.objects.filter(name='Orage').exists()
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        print(repr(serializer))
        return Response(serializer.data)
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25,min_length=5,write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password']

    def validate(self, attrs):
        username = attrs['username']
        
        if not username.isalnum():
            raise serializers.ValidationError("Enter username must be contain alpha-numeric value")
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = User    
        fields = ['token']


class LoginSerilaizer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200,write_only=True)
    username = serializers.CharField(max_length=200,read_only=True)
    token = serializers.CharField(max_length=555,read_only=True)
    
    class Meta:
        model = User
        fields = ['email','password','username','token']

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = authenticate(email=email,password=password)

        if not user:
            raise AuthenticationFailed("User is not Authenticated")
        
        if not user.is_verified:
            raise AuthenticationFailed("User is Not verify")
        
        if not user.is_active:
            raise AuthenticationFailed("User is not Active,Contact to Admin")

        user.save()
        return user
    
class PasswordResetEmailserilaizer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)

    class Meta:
        fields = ['email']

class PasswordResetComplateSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100,min_length=2,write_only=True)
    token = serializers.CharField(min_length=10,write_only=True)
    uid64 = serializers.CharField(min_length=1,write_only=True)

    class Meta:
        fields = ['password','token','uid64']

    def validate(self,data):
        try:
            password = data.get('password')
            token = data.get('token')
            uid64 = data.get('uid64')

            user_id = force_str(urlsafe_base64_decode(uid64))
            print(user_id)
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed("Token is not valided",404)
            
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            return Response({"msg":"Reset link invalid"})
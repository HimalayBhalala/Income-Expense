from django.shortcuts import render
import jwt.exceptions
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serilalizers import RegistrationSerializer,EmailVerifySerializer,LoginSerilaizer,PasswordResetEmailserilaizer,PasswordResetComplateSerializer
from rest_framework.response import Response
from .utils import Util
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from renderers import UserRenderer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,force_bytes,DjangoUnicodeDecodeError
from django.utils import encoding
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from app.utils import Util
from rest_framework.views import APIView

# Create your views here.

class RegisterView(GenericAPIView):
    serializer_class = RegistrationSerializer
    renderer_classes = [UserRenderer]

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            user_data = serializer.data

            user = User.objects.get(email=user_data['email'])

            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relative_path = reverse('email-verify')

            absurl = "http://"+current_site+relative_path+"?token="+str(token)

            email_body = f"Hi {user.username} Click Below url to for verify Your Email \n"+absurl

            data = {'email_body':email_body,'email_subject':"Verify-Email",'to':[user.email]}

            Util.send_email(data)

            return Response(serializer.data,status=status.HTTP_201_CREATED)


class EmailVerifyView(GenericAPIView):
    serializer_class = EmailVerifySerializer

    token_param_config = openapi.Parameter(
        'token',in_=openapi.IN_QUERY,description="Description",type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'msg':"Email Activate Successfully...."})
        except jwt.exceptions.ExpiredSignatureError as identifier:
            return Response({'msg':"Activation Expired"})
        except jwt.exceptions.DecodeError as identifier:
            return Response({'msg':"Invalid token"})
        
    
class LoginView(GenericAPIView):
    serializer_class = LoginSerilaizer

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        

class PasswordResetEmailView(GenericAPIView):
    serializer_class = PasswordResetEmailserilaizer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            uid64 = urlsafe_base64_encode(encoding.force_bytes(user.id))
            current_site = get_current_site(request).domain
            relativelink = reverse('password-reset-confirm',kwargs={'uid64':uid64,'token':token})
            absurl = "http://"+current_site+relativelink
            email_body = f"Hello,\n click below Link For reset the password\n"+absurl
            
            data = {'email_body':email_body,'email_subject':"Password Reset Verify",'to':[email]}

            Util.send_email(data)
            return Response({'success':"We have sent you link for reset a password"},status=status.HTTP_200_OK)

class PasswordTokenCheckAPI(APIView):
    def get(self,request,uid64,token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'message':"Your Credential is not valid"},status=status.HTTP_400_BAD_REQUEST)
            print(user_id)
            return Response({'success':True,'Credentials':'Valid','uid64':uid64,'token':token})
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator.check_token(user,token):
                return Response({'message':"Your Credential is not valid"},status=status.HTTP_400_BAD_REQUEST)
            
class SetNewPasswordApiView(GenericAPIView):
    serializer_class = PasswordResetComplateSerializer

    def patch(self,request):
        serializer = self.serializer_class(data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Reset Success'},status=status.HTTP_202_ACCEPTED)
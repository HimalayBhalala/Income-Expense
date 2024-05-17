from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView().as_view(),name='refresh'),
    path('email-verify/',views.EmailVerifyView.as_view(),name='email-verify'),
    path('reset-password-email/',views.PasswordResetEmailView.as_view(),name='reset-password-email'),
    path('password-reset/done/',views.SetNewPasswordApiView.as_view(),name='password-reset-done'),
    path('password-reset/<uid64>/<token>/',views.PasswordTokenCheckAPI.as_view(),name='password-reset-confirm')
]
                    
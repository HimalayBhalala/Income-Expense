from django.contrib.auth.models import BaseUserManager,UserManager

class UserManger(BaseUserManager):
    def create_user(self,username=None,email=None,password=None):
        if username is None:
            raise ValueError("Username is required")
        if email is None:
            raise ValueError("Email Must be required")
        
        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username=None,email=None,password=None):
        if password is None:
            raise ValueError("Password must be required")
        if email is None:
            raise ValueError("Email Must be required")
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user
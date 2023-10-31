from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    uses_in_migrations=True
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is required")
        user=self.model(email=email,**extra_fields)
        user=self.normalize_email(email)
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        pass
from django.db import models

# Create your models here.

class Login(models.Model):
    Email = models.EmailField(max_length=200, null=True, unique=True)
    Password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.Email} - {self.Password}"
    
class SignUp(models.Model):
    Username = models.CharField(max_length=170, null=True, unique=True)
    Email = models.EmailField(max_length=120, null=True, unique=True)
    Password = models.CharField(max_length=50, null=True)
    Confirm_Password = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f"{self.Username}-{self.Email}-{self.Password}-{self.Confirm_Password}"
from django.db import models

# Create your models here.

class UserSignUpModel(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField( max_length = 200)
    email = models.EmailField(unique=True,max_length=200,)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
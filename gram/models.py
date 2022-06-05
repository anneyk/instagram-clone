from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewUser(models.Model):
    OUR_CHOICES =(
    ("Mgr", "Manager"),
    ("Emp", "Employee"),
    ("Admin", "Administrator"),
    ("Sup", "Supervisor"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password1 = models.CharField(max_length=30, blank=True)
    password2 = models.CharField(max_length=30)

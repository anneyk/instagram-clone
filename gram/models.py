from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) 
  profile_pic = models.ImageField(upload_to='images/',default='default.png')
  bio = models.TextField(max_length=300, default='My bio',blank=True)
  name = models.CharField(max_length=30, blank=True)

  def __str__(self):
    return f'{self.user.username} Profile'
  
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()

  def save_profile(self):
    self.user

  def delete_profile(self):
    self.delete()

  @classmethod
  def search_profile(cls, name):
    return cls.objects.filter(user__username__icontains=name).all()
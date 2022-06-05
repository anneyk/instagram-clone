from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class NewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password1 = models.CharField(max_length=30, blank=True)
    password2 = models.CharField(max_length=30)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) 
  profile_picture = models.ImageField(upload_to='images/',default='default.png')
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

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Post'

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ["-pk"]
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	mobile=models.IntegerField(default=1)
	room=models.CharField(max_length=255,default=1)
	hostel=models.CharField(max_length=255,default=1)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'
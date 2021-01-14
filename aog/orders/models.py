from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
class Order(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	category = models.CharField(max_length=100)
	image=models.ImageField(default='default.jpg',upload_to='donated_pics')
	date_posted = models.DateTimeField(default=timezone.now)
	author =models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})


# Create your models here.

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=False)
	#photo = models.URLField(blank=True)
	#location = models.CharField(max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title

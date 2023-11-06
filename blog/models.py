from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 255)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	publishDate = models.DateTimeField()
	category = models.CharField(max_length = 255)

	def __str__(self):
		return self.name

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	author = models.CharField(max_length = 255)
	content = models.TextField()
	creationDate = models.DateTimeField()

	def __str__(self):
		return self.name

# Create your models here.

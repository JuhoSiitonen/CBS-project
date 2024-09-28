from django.db import models
from django.contrib.auth.models import User

class Posting(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	likes = models.IntegerField(default=0)
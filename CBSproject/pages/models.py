from django.db import models
from django.contrib.auth.models import User

class Posting(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	likes = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	posting = models.ForeignKey(Posting, on_delete=models.CASCADE)

	
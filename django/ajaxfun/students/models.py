
from django.db import models

class Student(models.Model):
	username = models.CharField(max_length=32)

	def __unicode__(self):
		return self.username


from django.db import models

class Student(models.Model):
	fullname = models.CharField(max_length=64)
	username = models.CharField(max_length=32)
	age = models.IntegerField()

	def __unicode__(self):
		return "%s (%s)" % (self.fullname, self.username)



from django.db import models

class Course(models.Model):
	name	 = models.CharField(max_length=32)
	description = models.CharField(max_length=256)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name',]

class Student(models.Model):
	name 	 = models.CharField(max_length=32)
	age		 = models.IntegerField(blank=True)
	email	 = models.EmailField()
	homepage = models.URLField(blank=True)
	courses	 = models.ManyToManyField(Course)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name',]


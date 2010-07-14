
from django.db import models

class Person(models.Model):
	GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
	)

	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

class University(models.Model):
	long_name = models.CharField(max_length=128)
	short_name = models.CharField(max_length=16)

	def __unicode__(self):
		return "%s (%s)" % (self.long_name, self.short_name)

class Student(models.Model):
	person = models.ForeignKey(Person)
	attends = models.ForeignKey(University)
#	courses = models.ManyToManyField(Course, verbose_name='List of courses')

	def __unicode__(self):
		return "%s %s" % (self.person.first_name, self.person.last_name)

class Course(models.Model):
	long_name = models.CharField(max_length=128)
	short_name = models.CharField(max_length=16)

	students = models.ManyToManyField(Student, 
			verbose_name='List of student taking this course', blank=True)

	def __unicode__(self):
		return "%s (%s)" % (self.long_name, self.short_name)


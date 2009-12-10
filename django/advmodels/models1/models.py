from django.db import models

class Course(models.Model):
	name         = models.CharField(max_length=16)
	display_name = models.CharField(max_length=128)
	last_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Student(models.Model):
	GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
	)

	first_name   = models.CharField(max_length=32)
	last_name    = models.CharField(max_length=32)
	gender       = models.CharField(max_length=2, choices=GENDER_CHOICES)
	age          = models.PositiveIntegerField()
	email        = models.EmailField()
	courses      = models.ManyToManyField(Course, blank=True)
	enrolled     = models.DateField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		ordering = ['last_name', 'first_name']

class Node(models.Model):
	name = models.CharField(max_length=32)
	parent = models.ForeignKey('self', blank=True, null=True)

	def __unicode__(self):
		return self.name

	def full_path(self):
		if self.parent == None:
			return self.name
		else:
			return self.parent.full_path() + "." + self.name


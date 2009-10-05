from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=64)
	addr = models.CharField(max_length=128)
	website = models.URLField(verify_exists=False)

	def __unicode__(self):
		return self.name

class Author(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	email = models.EmailField(blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
	title = models.CharField(max_length=64)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	pdf = models.FileField(upload_to='pdfs', blank=True)
	frontpage = models.ImageField(upload_to='images', blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['title']
	


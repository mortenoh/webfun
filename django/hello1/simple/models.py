from django.db import models

class Person(models.Model):
	COUNTRY_CHOICES = (
		(u'NO', 'Norway'),
		(u'SE', 'Sweden'),
		(u'DK', 'Denmark'),
	)
	
	GENDER_CHOICES = (
		(u'M', 'Male'),
		(u'F', 'Female'),
	)

	name = models.CharField(max_length=64)
#	birthdatetime = models.DateTimeField()
	birthdate = models.DateField()
#	birthtime = models.TimeField()
	birthcountry = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	homepage = models.URLField(verify_exists=False, blank=True)
	email = models.EmailField(blank=True)
	image = models.ImageField(upload_to='/tmp', blank=True)

	def __unicode__(self):
		return self.name

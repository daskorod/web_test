from django.db import models

class Topic(models.Model):
	'''Theme studied by user'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		'''return string repr of model'''
		return self.text

class Entry(models.Model):
	'''information studied by users'''
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		'''return string repr of model'''
		return self.text[:50] + '...'


# Create your models here.

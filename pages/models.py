from django.db import models
import datetime

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return "/pages/%i/" %self.id
from django.db import models 
from django.utils import timezone 


class contacts(models.Model):
	created_at = models.DateTimeField(default=timezone.now())
	phone_number = models.CharField(max_length=15,null=False)


	def __str__(self):
		return self.phone_number
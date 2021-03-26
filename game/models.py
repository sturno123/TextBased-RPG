from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=100)
	currentstage = models.IntegerField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name

class Stages(models.Model):
	text = models.TextField()
	A1 = models.TextField()
	A2 = models.TextField(blank=True, null=True)
	A3 = models.TextField(blank=True, null=True)
	A4 = models.TextField(blank=True, null=True)
	A5 = models.TextField(blank=True, null=True)
	A6 = models.TextField(blank=True, null=True)
	E1 = models.IntegerField(blank=True, null=True)
	E2 = models.IntegerField(blank=True, null=True)
	E3 = models.IntegerField(blank=True, null=True)
	E4 = models.IntegerField(blank=True, null=True)
	E5 = models.IntegerField(blank=True, null=True)
	E6 = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.text
	

		

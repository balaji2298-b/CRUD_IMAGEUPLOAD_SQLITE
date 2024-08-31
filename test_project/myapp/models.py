from django.db import models


class Blue(models.Model):
	name = models.CharField(max_length=20)
	phonenumber = models.CharField(max_length=20)
	email = models.CharField(max_length=10)
	image = models.ImageField(upload_to="picture/")

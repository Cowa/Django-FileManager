from django.db import models

class Folder(models.Model):
	name = models.CharField(max_lenght=30)
	# Folder's parent
	parent = models.ForeignKey(Folder)

class File(models.Model):
	name = models.CharField(max_lenght=30)
	content = models.CharField(max_lenght=500)
	# File's folder
	folder = models.ForeignKey(Folder)
from django.db import models

class Folder(models.Model):
	name = models.CharField(max_length=30)
	# Folder's parent
	parent = models.ForeignKey('self', null=True, blank=True)

	class Meta:
		# Two folders cannot have the same name if inside the same folder
		unique_together = ("name", "parent")

	def __unicode__(self):
		return self.name

class File(models.Model):
	name = models.CharField(max_length=30)
	content = models.CharField(max_length=500)
	# File's folder
	folder = models.ForeignKey(Folder)

	class Meta:
		# Two files cannot have the same name if inside the same folder
		unique_together = ("name", "folder")

	def __unicode__(self):
		return self.name

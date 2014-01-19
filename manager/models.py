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
	content = models.FileField(upload_to='files')
	# File's folder
	folder = models.ForeignKey(Folder)

	class Meta:
		# Two files cannot have the same name if inside the same folder
		unique_together = ("name", "folder")

	def __unicode__(self):
		return self.name

class FileLink(models.Model):
	name = models.CharField(max_length=30)
	link = models.CharField(max_length=150)
	# File link's folder
	folder = models.ForeignKey(Folder)

	class Meta:
		unique_together = ("name", "folder")

	def __unicode__(self):
		return self.name

class ShortcutFolder(models.Model):
	folder = models.ForeignKey(Folder)

	def __unicode__(self):
		return self.folder.name

class ShortcutFile(models.Model):
	file = models.ForeignKey(File)

	def __unicode__(self):
		return self.file.name

class ShortcutLink(models.Model):
	link = models.ForeignKey(FileLink)

	def __unicode__(self):
		return self.link.name

from django.contrib import admin
from manager.models import Folder, File

class FileInline(admin.StackedInline):
	model = File
	extra = 2

class FolderAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['name']}),
		('Parent', {'fields': ['parent']})
	]
	inlines = [FileInline]

admin.site.register(Folder, FolderAdmin)


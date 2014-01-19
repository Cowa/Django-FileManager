from django.contrib import admin
from manager.models import Folder, File, FileLink, ShortcutFolder, ShortcutFile, ShortcutLink

class FileInline(admin.StackedInline):
	model = File
	extra = 2

class FileLinkInline(admin.StackedInline):
	model = FileLink
	extra = 2

class FolderAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['name']}),
		('Parent', {'fields': ['parent']})
	]
	inlines = [FileInline, FileLinkInline]

admin.site.register(Folder, FolderAdmin)
admin.site.register(File)
admin.site.register(ShortcutFolder)
admin.site.register(ShortcutFile)
admin.site.register(ShortcutLink)

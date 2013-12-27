from django.shortcuts import render, get_object_or_404
from manager.models import Folder, File, ShortcutFolder, ShortcutFile, ShortcutLink

def index(request):
	# Get the root (must be unique or error)
	fold = get_object_or_404(Folder, parent=None)
	return folder(request, fold.id)

def folder(request, folder_id):
	folder = get_object_or_404(Folder, pk=folder_id)
	subfolders = Folder.objects.all().filter(parent=folder_id)
	files = File.objects.all().filter(folder=folder_id)
	shortcuts_folder = ShortcutFolder.objects.all()
	shortcuts_file = ShortcutFile.objects.all()
	shortcuts_link = ShortcutLink.objects.all()
	nb_items = len(subfolders) + len(files)
	context = {'path': folder, 'subfolders': subfolders, 'files': files, 'shortcuts_folder': shortcuts_folder, 'shortcuts_file': shortcuts_file, 'shortcuts_link': shortcuts_link, 'nb_items': nb_items}
	return render(request, 'manager/folder.html', context)

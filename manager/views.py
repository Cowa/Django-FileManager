from django.shortcuts import render, get_object_or_404
from manager.models import Folder, File

def index(request):
	# Get the root (must be unique or error)
	fold = get_object_or_404(Folder, parent=None)
	return folder(request, fold.id)

def folder(request, folder_id):
	folder = get_object_or_404(Folder, pk=folder_id)
	subfolders = Folder.objects.all().filter(parent=folder_id)
	files = File.objects.all().filter(folder=folder_id)
	context = {'path': folder, 'subfolders': subfolders, 'files': files}
	return render(request, 'manager/folder.html', context)

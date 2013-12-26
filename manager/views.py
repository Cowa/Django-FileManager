from django.shortcuts import render, get_object_or_404
from manager.models import Folder

def index(request):
	context = {'path': "/"}
	return render(request, 'manager/folder.html', context)

def test(request, folder_id):
	folder = get_object_or_404(Folder, pk=folder_id)
	context = {'path': folder}
	return render(request, 'manager/folder.html', context)

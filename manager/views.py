from django.shortcuts import render

def index(request):
	context = {'title': "Test Ditle"}
	return render(request, 'manager/index.html', context)

def test(request):
	context = {'title': "Test not Ditle"}
	return render(request, 'manager/index.html', context)

from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'index.html')

def ObjectsView(request):
    return render(request, 'objects.html')

def AddNewObjectView(request):
    return render(request, 'add_new_object.html')

def ObjectDetailView(request):
    return render(request, 'object_detail.html')

def login(request):
    return render(request, 'account/login.html')
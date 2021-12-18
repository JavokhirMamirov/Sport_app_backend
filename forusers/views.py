from django.shortcuts import render

def Index(request):
    return  render(request, 'users/index.html')

def ListObjects(request):
    return  render(request, 'users/objects.html')

def ObjectDetail(request):
    return render(request, 'users/object-detail.html')
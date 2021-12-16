from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def HomeView(request):
    return render(request, 'index.html')

def ObjectsView(request):
    return render(request, 'objects.html')

    
def AddNewObjectView(request):
    return render(request, 'add_new_object.html')

def ObjectDetailView(request):
    return render(request, 'object_detail.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect("/")

from types import resolve_bases
from typing import Type
from django.db.models.query_utils import select_related_descend
from django.forms.widgets import Select
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def HomeView(request):
    return render(request, 'index.html')


def ObjectsView(request):
    obj = SportObject.objects.all()
    category = Category.objects.all()
    req = request.GET.get('category')
    search = request.GET.get('q')
    
    if req != '' and req is not None:
        obj = obj.filter(category__id=req)
    elif search is not None and search != "":
        obj = obj.filter(name__icontains=search)
    page = request.GET.get('page')
    p = Paginator(obj, 2)
    pages = p.get_page(page)
    num_of_obj = 'a' * pages.paginator.num_pages
    context = {
        'pages':pages,
        'num_of_obj':num_of_obj,
        'category':category
    }
    return render(request, 'objects.html', context)


def AddNewObjectView(request):
    categories = Category.objects.all()
    types = ObjectType.objects.all()
    context = {
        "categories": categories,
        "types": types
    }
    return render(request, 'add_new_object.html', context)


def AddTypeUsers(request):
    if request.method == 'POST':
        form = ObjectTypeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('add-sport-object')


def AddObjectCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('add-sport-object')


def ObjectDetailView(request, pk):
    object = SportObject.objects.get(id=pk)
    context = {
        'object':object,
    }
    return render(request, 'object_detail.html', context)


def DeleteObjectView(request):
    object = request.GET.get('object_id')
    delete_object = SportObject.objects.get(id=object)
    delete_object.delete()
    return redirect('sport-object')


def UpdateObjectView(request, pk):
    form = SportObject.objects.get(id=pk)
    categories = Category.objects.all()
    types = ObjectType.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'types':types
    }
    return render(request, 'update-object.html', context)


# Auth system
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


def CreateObject(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            description = request.POST['description']
            images = request.FILES.getlist('images')
            location = request.POST['location']
            address = request.POST['address']
            phone = request.POST['phone']
            work_date = request.POST['work_date']
            area = request.POST['area']
            category = request.POST.getlist('category')
            invent_date = request.POST['invent_date']
            type = request.POST['type']
            date_start = request.POST['date_start']
            date_end = request.POST['date_end']
            shower = request.POST['shower']
            changing_room = request.POST['changing_room']
            lighting = request.POST['lighting']
            tribunes = request.POST['tribunes']
            parking = request.POST['parking']
            is_active = request.POST['is_active']
            if shower == "on":
                shower = True
            else:
                shower = False

            if changing_room == "on":
                changing_room = True
            else:
                changing_room = False

            if lighting == "on":
                lighting = True
            else:
                lighting = False

            if parking == "on":
                parking = True
            else:
                parking = False

            if tribunes == "on":
                tribunes = True
            else:
                tribunes = False

            if is_active == "on":
                is_active = True
            else:
                is_active = False

            #create image
            obj = SportObject.objects.create(
                name=name, address=address, phone=phone, date_start=date_start,
                date_end=date_end, work_date=work_date, area=area,
                invent_date=invent_date, shower=shower, lighting=lighting,
                tribunes=tribunes, parking=parking, location=location,
                type_id=type, description=description, is_active=is_active,
                changing_room=changing_room
            )
            try:
                for image in images:
                    img = Images.objects.create(image=image)
                    obj.images.add(img)
                for cat in category:
                    try:
                        ct = Category.objects.get(id=cat)
                        obj.category.add(ct)
                    except:
                        pass
            except:
                obj.delete()
                messages.error(request, "Obyekt yaratishda xatolik!")
                return redirect('add-sport-object')

            messages.success(request, "Obyekt yaratildi!")
            return redirect('sport-object')

        except Exception as err:
            print(err)
            messages.error(request, "Obyekt yaratishda xatolik!")
            return redirect('add-sport-object')
    else:
        return redirect('add-sport-object')



def UpdateObject(request, id):
    if request.method == "POST":
        object = SportObject.objects.get(id=id)
        try:
            name = request.POST['name']
            description = request.POST['description']
            location = request.POST['location']
            address = request.POST['address']
            phone = request.POST['phone']
            work_date = request.POST['work_date']
            area = request.POST['area']
            category = request.POST.getlist('category')
            invent_date = request.POST['invent_date']
            type = request.POST['type']
            print(type)
            date_start = request.POST['date_start']
            date_end = request.POST['date_end']
            shower = request.POST['shower']
            changing_room = request.POST['changing_room']
            lighting = request.POST['lighting']
            tribunes = request.POST['tribunes']
            parking = request.POST['parking']
            is_active = request.POST['is_active']
            if shower == "on":
                shower = True
            else:
                shower = False

            if changing_room == "on":
                changing_room = True
            else:
                changing_room = False

            if lighting == "on":
                lighting = True
            else:
                lighting = False

            if parking == "on":
                parking = True
            else:
                parking = False

            if tribunes == "on":
                tribunes = True
            else:
                tribunes = False

            if is_active == "on":
                is_active = True
            else:
                is_active = False
            object.name=name
            object.address=address
            object.phone=phone
            object.date_start=date_start
            object.date_end=date_end
            object.work_date=work_date 
            object.area=area
            object.invent_date=invent_date 
            object.shower=shower
            object.lighting=lighting
            object.tribunes=tribunes 
            object.parking=parking
            object.location=location
            object.type_id=type
            object.description=description 
            object.is_active=is_active
            object.changing_room=changing_room
            object.save()
            for cat in category:
                try:
                    ct = Category.objects.get(id=cat)
                    object.category.add(ct)
                    object.save()
                    return redirect('sport-object')
                except:
                    messages.error(request, "Obyekt yangilashda xatolik1!")
                    return redirect('sport-object')
        except:
            messages.error(request, "Obyekt yangilashda xatolik2!")
            return redirect('sport-object')
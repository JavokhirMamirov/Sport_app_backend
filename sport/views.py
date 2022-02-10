from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from sport.models import Orders
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list

@login_required(login_url='login')
def HomeView(request):
    if request.user.is_staff == True:            
        category = Category.objects.all().count()
        object = SportObject.objects.all().count()
        active = SportObject.objects.filter(is_active=True).count()
        false = SportObject.objects.filter(is_active=False).count()
        new = Orders.objects.filter(is_active='new').count()
        accepted = Orders.objects.filter(is_active='accepted').count()
        not_accepted = Orders.objects.filter(is_active='not_accepted').count()
        alert = ['primary', 'success', 'danger', "info", "warning"]
        cats = Category.objects.all()
        cat_list = []
        k = 0
        for cat in cats:
            obj_count = SportObject.objects.filter(category__in=[cat]).count()
            dt = {
                "id":cat.id,
                "name":cat.name,
                "obj_count":obj_count,
                "color":alert[k]
            }
            k += 1
            if k == 5:
                k = 0
            cat_list.append(dt) 
        context = {
            'category':category,
            'cat_lists':cat_list,
            'object':object,
            'active':active,
            'false':false,
            'new':new,
            'accepted':accepted,
            'not_accepted':not_accepted        
        }
        return render(request, 'index.html', context)
    else:
        if request.method == 'POST':
            user_object = request.POST['chekname']
            object = SportObject.objects.get(id=user_object)
            object.follower.add(request.user) 
            object.save()
            return redirect('home')
        else:
            empty_objects = []
            choised_objects = []
            for i in SportObject.objects.all():
                if request.user in i.follower.all():
                    choised_objects.append(i)
                else:
                    empty_objects.append(i)
        context = {
            'objects': empty_objects,
            'choised_objects':choised_objects,
        }
        return render (request, 'account/dashboard.html', context)

        
@login_required(login_url='login')
def ObjectsView(request):
    obj = SportObject.objects.all()
    category = Category.objects.all()
    req = request.GET.get('category')
    search = request.GET.get('q')

    if req != '' and req is not None:
        obj = obj.filter(category__in=[req])
    elif search is not None and search != "":
        obj = obj.filter(name__icontains=search)
    context = {
        'category': category,
        'objects': PagenatorPage(obj, 10, request)
    }
    return render(request, 'objects.html', context)

@login_required(login_url='login')
def AddNewObjectView(request):
    categories = Category.objects.all()
    types = ObjectType.objects.all()
    context = {
        "categories": categories,
        "types": types
    }
    return render(request, 'add_new_object.html', context)

@login_required(login_url='login')
def AddTypeUsers(request):
    if request.method == 'POST':
        form = ObjectTypeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('add-sport-object')

@login_required(login_url='login')
def AddObjectCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('add-sport-object')

@login_required(login_url='login')
def ObjectDetailView(request, pk):
    object = SportObject.objects.get(id=pk)
    context = {
        'object': object,
    }
    return render(request, 'object_detail.html', context)

@login_required(login_url='login')
def DeleteObjectView(request):
    object = request.GET.get('object_id')
    delete_object = SportObject.objects.get(id=object)
    delete_object.delete()
    return redirect('sport-object')

@login_required(login_url='login')
def UpdateObjectView(request, pk):
    form = SportObject.objects.get(id=pk)
    categories = Category.objects.all()
    types = ObjectType.objects.all()
    context = {
        'form': form,
        'categories': categories,
        'types': types
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
    return redirect("index_url")

@login_required(login_url='login')
def CreateObject(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            description = request.POST['description']
            images = request.FILES.getlist('images')
            lat = request.POST['lat']
            lng = request.POST['lng']
            address = request.POST['address']
            phone = request.POST['phone']
            work_date = request.POST['work_date']
            area = request.POST['area']
            category = request.POST.getlist('category')
            invent_date = request.POST['invent_date']
            type = request.POST['type']
            date_start = request.POST['date_start']
            date_end = request.POST['date_end']
            shower = request.POST.get('shower')
            changing_room = request.POST.get('changing_room')
            lighting = request.POST.get('lighting')
            tribunes = request.POST.get('tribunes')
            parking = request.POST.get('parking')
            is_active = request.POST.get('is_active')
            if shower is not None:
                shower = True
            else:
                shower = False

            if changing_room is not None:
                changing_room = True
            else:
                changing_room = False

            if lighting is not None:
                lighting = True
            else:
                lighting = False

            if parking is not None:
                parking = True
            else:
                parking = False

            if tribunes is not None:
                tribunes = True
            else:
                tribunes = False

            if is_active is not None:
                is_active = True
            else:
                is_active = False

            # create image
            obj = SportObject.objects.create(
                name=name, address=address, phone=phone, date_start=date_start,
                date_end=date_end, work_date=work_date, area=area,
                invent_date=invent_date, shower=shower, lighting=lighting,
                tribunes=tribunes, parking=parking, lat=lat, lng=lng,
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

@login_required(login_url='login')
def UpdateObject(request, id):
    if request.method == "POST":
        object = SportObject.objects.get(id=id)
        try:
            name = request.POST['name']
            description = request.POST['description']
            lat = request.POST['lat']
            lng = request.POST['lng']
            address = request.POST['address']
            phone = request.POST['phone']
            work_date = request.POST['work_date']
            area = request.POST['area']
            category = request.POST.getlist('category')
            invent_date = request.POST['invent_date']
            type = request.POST['type']
            date_start = request.POST['date_start']
            date_end = request.POST['date_end']
            shower = request.POST.get('shower')
            changing_room = request.POST.get('changing_room')
            lighting = request.POST.get('lighting')
            tribunes = request.POST.get('tribunes')
            parking = request.POST.get('parking')
            is_active = request.POST.get('is_active')
            if shower is not None:
                shower = True
            else:
                shower = False

            if changing_room is not None:
                changing_room = True
            else:
                changing_room = False

            if lighting is not None:
                lighting = True
            else:
                lighting = False

            if parking is not None:
                parking = True
            else:
                parking = False

            if tribunes is not None:
                tribunes = True
            else:
                tribunes = False

            if is_active is not None:
                is_active = True
            else:
                is_active = False
            object.name = name
            object.address = address
            object.phone = phone
            object.date_start = date_start
            object.date_end = date_end
            object.work_date = work_date
            object.area = area
            object.invent_date = invent_date
            object.shower = shower
            object.lighting = lighting
            object.tribunes = tribunes
            object.parking = parking
            object.lat = lat
            object.lng = lng
            object.type_id = type
            object.description = description
            object.is_active = is_active
            object.changing_room = changing_room

            for cat in category:
                object.category.clear()
                try:
                    ct = Category.objects.get(id=cat)
                    object.category.add(ct)

                except:
                    messages.error(request, "Obyekt yangilashda xatolik1!")
            object.save()
            return redirect('sport-object-detail', pk=object.id)
# images
        except:
            messages.error(request, "Obyekt yangilashda xatolik2!")
            return redirect('sport-object-detail', pk=id)

@login_required(login_url='login')
def add_image(request):
    try:
        object_id = request.POST.get('object_id')
        img = request.FILES.get('img')
        image = Images.objects.create(image=img)
        obj = SportObject.objects.get(id=object_id)
        obj.images.add(image)
        obj.save()
        context = {
            "success": True
        }
    except:
        context = {
            "success": False
        }
    return JsonResponse(context)

@login_required(login_url='login')
def delete_image(request):
    try:
        object_id = request.GET.get('object_id')
        image_id = request.GET.get('image_id')
        obj = SportObject.objects.get(id=object_id)
        image = Images.objects.get(id=image_id)
        obj.images.remove(image)
        obj.save()
        context = {
            "success": True
        }
    except:
        context = {
            "success": False
        }
    return JsonResponse(context)

def notf(request):
    return render(request, 'errors/404.html')


def server(request):
    return render(request, 'errors/500.html')

def order_new(request):
    count = Orders.objects.filter(is_active='new').count()
    object = Orders.objects.filter(is_active='new')
    context = {
        'count':count,
        'object':object
    }
    return render(request, 'order-new.html', context)


def order_accepted(request):
    count = Orders.objects.filter(is_active='accepted').count()
    object = Orders.objects.filter(is_active='accepted')
    context = {
        'count':count,
        'object':object
    }
    return render(request, 'order-accepted.html', context)


def order_not_accepted(request):
    count = Orders.objects.filter(is_active='not_accepted').count()
    object = Orders.objects.filter(is_active='not_accepted')
    context = {
        'count':count,
        'object':object
    }
    return render(request, 'order-not_accepted.html', context)

def delete_order(request):
    try:
        order = request.GET.get('object_id')
        delete_order = Orders.objects.get(id=order)
        delete_order.delete()
        return redirect('home')
    except:
        return HttpResponse(False)

def change_order(request, pk):
    order = Orders.objects.get(id=pk)
    rad = request.POST.get('RAD')
    qabul = request.POST.get('QABUL')
    if rad is not None:
        order.is_active = 'not_accepted'
    elif qabul is not None:
        order.is_active = 'accepted'
    order.save()   
    return redirect('home')
    
def user_create(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                login(request, new_user)
            else:
                messages.error(request, 'Parolingizni takrorlashda xatolik ro`y berdi')
        except:
            messages.error(request, 'Xatolik ro`y berdi')
    else:
        pass
    return render(request, 'account/signup.html')

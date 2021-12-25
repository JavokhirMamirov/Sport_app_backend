from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from sport.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import OrderForm

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


def Index(request):
    objects = SportObject.objects.filter(is_active=True)[:5]
    object = SportObject.objects.filter(is_active=True).first()
    categories = Category.objects.all()
    obyekt_soni = SportObject.objects.all().count()
    categoriyalar_soni = Category.objects.all().count()
    context = {
        'objects': objects,
        'categories': categories,
        'object': object,
        'obyekt_soni': obyekt_soni,
        'categoriyalar_soni': categoriyalar_soni
    }
    return render(request, 'users/index.html', context)


def ListObjects(request):
    objects = SportObject.objects.all()
    category = Category.objects.all()
    req = request.GET.get('category')
    search = request.GET.get('q')

    if req != '' and req is not None:
        objects = objects.filter(category__in=[req])
    elif search is not None and search != "":
        objects = objects.filter(name__icontains=search)
    context = {
        'objects': PagenatorPage(objects, 5, request),
        'category': category
    }
    return render(request, 'users/objects.html', context)


def ObjectDetail(request, pk):
    object = SportObject.objects.get(id=pk)
    return render(request, 'users/object-detail.html', {'object': object})


def OrderSave(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        object_name = request.POST['object_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        try:
            Orders.objects.create(
            full_name=full_name, 
            object_name=object_name,
            address=address,
            phone=phone,
            email=email
            )
            return redirect('objects_url')
        except:
            return HttpResponse(False)
    else:
        return redirect('index_url')
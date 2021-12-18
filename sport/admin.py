from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Images)


@admin.register(SportObject)
class SportObjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "address",
        "phone",
        "date_start",
        "date_end",
        "work_date",
        "area",
        "invent_date",
        "shower",
        "changing_room",
        "lighting",
        "tribunes",
        "parking",
        "lat",
        'lng',
        "type"
    ]

admin.site.register(ObjectType)

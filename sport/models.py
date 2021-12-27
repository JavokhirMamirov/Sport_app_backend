from django.db import models


# Create your models here.
from location_field.models.plain import PlainLocationField


class Category(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='images/')


class ObjectType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SportObject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi") 
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Manzili") 
    phone = models.CharField(max_length=255, verbose_name="Telefon raqami") 
    date_start = models.TimeField(verbose_name="Ochilish vaqti", null=True, blank=True) 
    date_end = models.TimeField(verbose_name="Yopilish vaqti", null=True, blank=True) 
    work_date = models.CharField(max_length=255,verbose_name="ISh kunlari", null=True, blank=True) 
    area = models.CharField(max_length=30, null=True, blank=True) 
    images = models.ManyToManyField(Images, blank=True)
    category = models.ManyToManyField(Category, blank=True) 
    invent_date = models.DateField(null=True, blank=True) 
    shower = models.BooleanField(default=False, verbose_name='Yuvunish xonasi') 
    changing_room = models.BooleanField(default=False, verbose_name="Kiyim almashtirish xonasi") 
    lighting = models.BooleanField(default=False, verbose_name="Yoritish chiroqlari") 
    tribunes = models.BooleanField(default=False, verbose_name="O'rindiqlar") 
    parking = models.BooleanField(default=False, verbose_name="Parkovka") 
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    type = models.ForeignKey(ObjectType, on_delete=models.CASCADE, null=True, blank=True) 
    description = models.TextField(null=True, blank=True) 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sport obyekti"
        verbose_name_plural = "Sport obyektlari"


class Orders(models.Model):
    CHOICE = (
    ('new','new'),
    ('accepted','accepted'),
    ('not_accepted','not_accepted'),
    )
    full_name = models.CharField(max_length=255, verbose_name='to`liq ism')
    object_name = models.CharField(max_length=255, verbose_name='obyekt nomi')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, verbose_name="Telefon raqami") 
    email = models.EmailField()
    is_active = models.CharField(max_length=255, choices=CHOICE, default='new')

    def __str__(self):
        return self.object_name

        
    
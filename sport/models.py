from django.db import models


# Create your models here.
from location_field.models.plain import PlainLocationField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='images/')


class ObjectType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SportObject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi") #ok
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Manzili") #ok
    phone = models.CharField(max_length=255, verbose_name="Telefon raqami") #ok
    date_start = models.TimeField(verbose_name="Ochilish vaqti", null=True, blank=True) #ok
    date_end = models.TimeField(verbose_name="Yopilish vaqti", null=True, blank=True) #ok
    work_date = models.CharField(max_length=255,verbose_name="ISh kunlari", null=True, blank=True) #ok
    area = models.CharField(max_length=30, null=True, blank=True) #ok
    images = models.ManyToManyField(Images, blank=True)
    category = models.ManyToManyField(Category, blank=True) #ok
    invent_date = models.DateField(null=True, blank=True) #ok
    shower = models.BooleanField(default=False, verbose_name='Yuvunish xonasi') #ok
    changing_room = models.BooleanField(default=False, verbose_name="Kiyim almashtirish xonasi") #ok
    lighting = models.BooleanField(default=False, verbose_name="Yoritish chiroqlari") #ok
    tribunes = models.BooleanField(default=False, verbose_name="O'rindiqlar") #ok
    parking = models.BooleanField(default=False, verbose_name="Parkovka") #ok
    location = PlainLocationField(based_fields=['city'], zoom=7) #ok
    type = models.ForeignKey(ObjectType, on_delete=models.CASCADE, null=True, blank=True) #ok
    description = models.TextField(null=True, blank=True) #ok
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sport obyekti"
        verbose_name_plural = "Sport obyektlari"






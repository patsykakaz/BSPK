#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to

from colorfield.fields import ColorField

# HOME
class Home(Page):
    baseline = models.TextField(default=False,null=False,blank=True)
    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Home, self).save(*args, **kwargs)

class Home_picture(models.Model):
    Home = models.ForeignKey('home')
    # image = models.ImageField(upload_to=MEDIA_ROOT+'/home', verbose_name='Home illustration')
    image = FileField(verbose_name=_("illustration Home"),
        upload_to=upload_to("static.media.uploads", "home"),
        format="Image", max_length=255, null=True, blank=True)

# FOOD
class Food_category(Page):
    # color = ColorField(default='#007099')
    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Food_category, self).save(*args, **kwargs)

class Food(models.Model):
    Food_category = models.ForeignKey("Food_category")
    name = models.CharField(max_length=150)
    price = models.IntegerField()

# DRINKS
class Drink_category(Page):
    half_display_size = models.BooleanField(default=False,null=False,blank=False,verbose_name='Coche la case si cette catégorie de boisson doit apparaitre sur la moitié de la page au lieu de la largeur total, batard')
   
    def save(self, *args, **kwargs):
        self.in_menus = []
        super(Drink_category, self).save(*args, **kwargs)

class Drink(models.Model):
    Drink_category = models.ForeignKey("Drink_category")
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField(default=False,null=False,blank=False)

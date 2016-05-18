#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

class Home_pictureInline(admin.TabularInline):
    model = Home_picture
HomeFieldsets = deepcopy(PageAdmin.fieldsets)
HomeFieldsets[0][1]["fields"].insert(-2, "baseline")
class HomeAdmin(PageAdmin):
    inlines = (Home_pictureInline,)
    fieldsets = HomeFieldsets

class FoodInline(admin.TabularInline):
    model = Food
class Food_categoryAdmin(PageAdmin):
    inlines = (FoodInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets)

Drink_categoryAdmin_extra_fieldsets = (
                (None,
                        {'fields': ('half_display_size',)
                        }
                ),
        )
class DrinkInline(admin.TabularInline):
    model = Drink
class Drink_categoryAdmin(PageAdmin):
    inlines = (DrinkInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + Drink_categoryAdmin_extra_fieldsets

admin.site.register(Home, HomeAdmin)
admin.site.register(Food_category, Food_categoryAdmin)
admin.site.register(Drink_category, Drink_categoryAdmin)


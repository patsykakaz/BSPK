#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from mezzanine.conf import settings
from models import *

import itertools


class CustomMiddleware(object):
    def process_template_response(self, request, response):
        home = Home.objects.last()
        homePicture = Home_picture.objects.filter(Home=home).last()
        baseline = home.baseline
        print baseline
        foodCat = Food_category.objects.all()
        for cat in foodCat: 
            cat.food = Food.objects.filter(Food_category=cat)
        drinkCat = Drink_category.objects.all()
        for cat in drinkCat: 
            cat.drinks = Drink.objects.filter(Drink_category=cat)
        response.context_data['baseline'] = baseline
        response.context_data['homePicture'] = homePicture
        response.context_data['foodCat'] = foodCat
        response.context_data['drinkCat'] = drinkCat
        return response




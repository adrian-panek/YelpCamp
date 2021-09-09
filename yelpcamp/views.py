import random

from django.shortcuts import render
from django.http import HttpResponse

from .models import Campground
from seeds import cities, names

def seedDB(request):
    Campground.objects.all().delete()
    for i in range(0,5):
        campground = Campground()
        rand_index_place = random.randint(0,49)
        rand_index_name = random.randint(0,15)
        random_city = cities.cities[rand_index_place]
        random_cityname = random_city["city"]
        random_state = random_city["state"]
        random_descriptor = names.descriptors[rand_index_name]
        random_place = names.places[rand_index_name]
        campground_random_title = (f"{random_descriptor} {random_place}")
        campground_random_location = (f"{random_cityname}, {random_state}")
        campground.title = campground_random_title
        campground.location = campground_random_location
        campground.save()
    return HttpResponse ("<h1>Database seed</h1>")

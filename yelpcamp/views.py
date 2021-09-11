import random
from typing import ContextManager

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Campground
from .forms import CampgroundForm
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

def HomePage(request):
    campgrounds = Campground.objects.all()
    return render(request, 'yelpcamp/index.html', {'campgrounds': campgrounds})

def ShowPage(request, id):
    campground = Campground.objects.get(id=id)
    return render(request, 'yelpcamp/show.html', {'campground': campground})

def NewCampground(request):
    form = CampgroundForm()
    if request.method == 'POST':
        print(f"Printing POST: {request.POST}")
        form = CampgroundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("campgrounds-list")
    context = {'form': form}
    return render (request, 'yelpcamp/new.html', context)

def UpdatePage(request, id):
    campground = Campground.objects.get(id=id)
    form = CampgroundForm(instance=campground)
    if request.method == 'POST':
        form = CampgroundForm(request.POST, instance=campground)
        if form.is_valid():
            form.save()
            return redirect("campgrounds-list")
    context = {'form': form}
    return render(request, 'yelpcamp/edit.html', context)

def DeletePage(request, id):
    campground = Campground.objects.get(id=id)
    if request.method == 'POST':
        campground.delete()
        return redirect("campgrounds-list")
    context = {'campground': campground}
    return render(request, 'yelpcamp/delete.html', context)
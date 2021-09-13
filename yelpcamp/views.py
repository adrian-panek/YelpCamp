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
        campground.image = "https://images.unsplash.com/photo-1484815843298-2c13cbc1b66f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHw0ODMyNTF8fHx8fHx8MTYzMTU1MTkwNQ&ixlib=rb-1.2.1&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080"
        campground.description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit laudantium eos nihil repudiandae incidunt quidem iure neque provident aperiam vero eum quas saepe fuga veniam, exercitationem, iste maxime itaque quam.'
        campground.save()
    return HttpResponse ("<h1>Database seed</h1>")

def HomePage(request):
    return render(request, 'home.html')

def IndexPage(request):
    campgrounds = Campground.objects.all()
    return render(request, 'index.html', {'campgrounds': campgrounds})

def ShowPage(request, id):
    campground = Campground.objects.get(id=id)
    return render(request, 'show.html', {'campground': campground})

def NewCampground(request):
    form = CampgroundForm()
    if request.method == 'POST':
        print(f"Printing POST: {request.POST}")
        form = CampgroundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("campgrounds-list")
    context = {'form': form}
    return render (request, 'new.html', context)

def UpdatePage(request, id):
    campground = Campground.objects.get(id=id)
    form = CampgroundForm(instance=campground)
    if request.method == 'POST':
        form = CampgroundForm(request.POST, instance=campground)
        if form.is_valid():
            form.save()
            return redirect("campgrounds-list")
    context = {'form': form}
    return render(request, 'edit.html', context)

def DeletePage(request, id):
    campground = Campground.objects.get(id=id)
    if request.method == 'POST':
        campground.delete()
        return redirect("campgrounds-list")
    context = {'campground': campground}
    return render(request, 'delete.html', context)
from django.urls import path

from .views import *

urlpatterns = [ 
    path('seeddb/', seedDB),
    path('', HomePage, name="homepage"),
    
    path('login', LoginPage, name="login"),
    path('logout', LogoutPage, name="logout"),
    path('register', RegisterPage, name="register"),

    path('campgrounds/', IndexPage, name="campgrounds-list"),
    path('campgrounds/new', NewCampground, name="campground-new"),
    path('campgrounds/<int:id>/', ShowPage, name="campground-detail"),
    path('campgrounds/<int:id>/update', UpdatePage, name="campground-update"),
    path('campgrounds/<int:id>/delete', DeletePage, name="campground-delete")
]


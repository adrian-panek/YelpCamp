from django.urls import path

from .views import HomePage, IndexPage, ShowPage, NewCampground, UpdatePage, DeletePage, seedDB

urlpatterns = [ 
    path('seeddb/', seedDB),
    path('', HomePage, name="homepage"),
    path('campgrounds/', IndexPage, name="campgrounds-list"),
    path('campgrounds/new', NewCampground, name="campground-new"),
    path('campgrounds/<int:id>/', ShowPage, name="campground-detail"),
    path('campgrounds/<int:id>/update', UpdatePage, name="campground-update"),
    path('campgrounds/<int:id>/delete', DeletePage, name="campground-delete")
]


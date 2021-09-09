from django.urls import path

from .views import seedDB

urlpatterns = [ 
    path('seeddb/', seedDB)
]
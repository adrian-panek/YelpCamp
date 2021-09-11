from django.forms import ModelForm

from .models import Campground

class CampgroundForm(ModelForm):
    class Meta:
        model = Campground
        fields = '__all__'
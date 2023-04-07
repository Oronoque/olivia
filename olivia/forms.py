from django import forms
from django.contrib.auth import get_user_model
from .models import Routine


class RoutineStepForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('name', 'user')

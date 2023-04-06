from django import forms
from django.contrib.auth import get_user_model
from .models import Routine


class RoutineForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all())

    class Meta:
        model = Routine
        fields = ['name', 'user']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if not isinstance(user, get_user_model()):
            raise forms.ValidationError('Invalid user')
        return user

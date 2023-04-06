from django.contrib import admin
from .forms import RoutineForm
from .models import Routine, RoutineSteps


admin.site.register(Routine)
admin.site.register(RoutineSteps)

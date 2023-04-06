from django.contrib import admin
from .forms import RoutineForm
from .models import Routine, RoutineSteps
from django.contrib.auth import get_user_model


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = get_user_model().objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(RoutineSteps)

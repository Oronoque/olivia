from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Routine


class CreateRoutineView(LoginRequiredMixin, CreateView):
    model = Routine
    template_name = 'create_routine.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

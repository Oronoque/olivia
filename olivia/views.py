from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from olivia.models import Routine, RoutineSteps
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from olivia.models import Routine, RoutineSteps
from olivia.forms import RoutineStepForm
from django.http import Http404



# Vista para listar todas las rutinas
class RoutineListView(ListView):
    model = Routine
    template_name = 'routine_list.html'

# Vista para crear una nueva rutina
class RoutineCreateView(CreateView):
    model = Routine
    fields = ['name', 'user']
    success_url = reverse_lazy('routine_list')
    template_name = 'routine_form.html'

# Vista para actualizar una rutina existente
class RoutineUpdateView(UpdateView):
    model = Routine
    fields = ['name', 'user']
    success_url = reverse_lazy('routine_list')
    template_name = 'routine_form.html'

# Vista para eliminar una rutina
class RoutineDeleteView(DeleteView):
    model = Routine
    success_url = reverse_lazy('routine_list')
    template_name = 'routine_confirm_delete.html'

# Vista para listar los pasos de una rutina en formato JSON
def routine_step_list(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    steps = routine.steps.all().order_by('order')
    data = list(steps.values('id', 'description', 'order'))
    return JsonResponse(data, safe=False)

# Vista para actualizar el orden de los pasos de una rutina
def routine_step_order(request):
    if request.method == 'POST':
        new_order = request.POST.getlist('order[]')
        for i, pk in enumerate(new_order):
            step = get_object_or_404(RoutineSteps, pk=pk)
            step.order = i
            step.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid method'})



class RoutineStepListView(ListView):
    model = RoutineSteps
    template_name = 'routine_step_list.html'

    def get_queryset(self):
        routine_pk = self.kwargs['pk']
        routine = get_object_or_404(Routine, pk=routine_pk, user=self.request.user)
        queryset = RoutineSteps.objects.filter(routine=routine)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        routine_pk = self.kwargs['pk']
        routine = get_object_or_404(Routine, pk=routine_pk, user=self.request.user)
        context['routine'] = routine
        context['csrf_token'] = self.request.COOKIES['csrftoken']
        context['steps'] = RoutineSteps.objects.filter(routine=routine)
        return context

class RoutineStepCreateView(LoginRequiredMixin, CreateView):
    model = RoutineSteps
    template_name = 'routine_step_form.html'
    form_class = RoutineStepForm

    def get_form_kwargs(self):
        kwargs = super(RoutineStepCreateView, self).get_form_kwargs()
        kwargs['routine_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        routine_pk = self.kwargs['pk']
        routine = get_object_or_404(Routine, pk=routine_pk, user=self.request.user)
        routine_step = form.save(commit=False)
        routine_step.routine = routine
        routine_step.save()
        return super().form_valid(form)

class RoutineStepUpdateView(LoginRequiredMixin, UpdateView):
    model = RoutineSteps
    template_name = 'routine_step_form.html'
    form_class = RoutineStepForm

    def get_object(self, queryset=None):
        obj = super(RoutineStepUpdateView, self).get_object()
        if not obj.routine.user == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse_lazy('routine_step_list', kwargs={'pk': self.object.routine.pk})

class RoutineStepDeleteView(LoginRequiredMixin, DeleteView):
    model = RoutineSteps
    template_name = 'routine_step_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(RoutineStepDeleteView, self).get_object()
        if not obj.routine.user == self.request.user:
            raise  
        return obj

    def get_success_url(self):
        return reverse_lazy('routine_step_list', kwargs={'pk': self.object.routine.pk})
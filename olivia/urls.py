from django.urls import path
from .views import RoutineListView, RoutineCreateView, RoutineUpdateView, RoutineDeleteView, \
    RoutineStepListView, RoutineStepCreateView, RoutineStepUpdateView, RoutineStepDeleteView

app_name = 'myapp'

urlpatterns = [
    path('routines/', RoutineListView.as_view(), name='routine_list'),
    path('routine/create/', RoutineCreateView.as_view(), name='routine_create'),
    path('routine/<int:pk>/update/', RoutineUpdateView.as_view(), name='routine_update'),
    path('routine/<int:pk>/delete/', RoutineDeleteView.as_view(), name='routine_delete'),
    path('routine/<int:pk>/steps/', RoutineStepListView.as_view(), name='routine_step_list'),
    path('routine/<int:pk>/step/create/', RoutineStepCreateView.as_view(), name='routine_step_create'),
    path('routine/step/<int:pk>/update/', RoutineStepUpdateView.as_view(), name='routine_step_update'),
    path('routine/step/<int:pk>/delete/', RoutineStepDeleteView.as_view(), name='routine_step_delete'),
]

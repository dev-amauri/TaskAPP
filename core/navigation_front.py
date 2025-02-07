from django.urls import path

from core.views import render_template

urlpatterns = [
    path('', lambda request: render_template(request, 'home.html'), name='home'),
    path('tasks', lambda request: render_template(request, 'task_list.html'), name='task_list'),
    path('tasks/details', lambda request: render_template(request, 'details_task.html'), name='task_create'),
    path('tasks/details/<int:pk>', lambda request, pk: render_template(request, 'details_task.html', pk), name='task_edit'),
    path('crud', lambda request: render_template(request, 'task_crud.html'), name='task_list'),
]
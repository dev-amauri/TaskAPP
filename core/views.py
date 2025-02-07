from rest_framework import viewsets
from core.models import Task
from core.serializers import TaskSerializers
from django.shortcuts import render, get_object_or_404
from django.http import Http404


#Vista de renderizado de html


def render_template(request, template_name, pk=None):
    context = {}
    if pk:
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
    return render(request, template_name, context)

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
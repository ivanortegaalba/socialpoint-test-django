from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.utils.timezone import now
from django.utils.encoding import smart_str
from celery.task.control import inspect
import json
from .models import Task
from .forms import TaskForm
from .task import *
# Create your views here.

class IndexView(ListView):
    template_name= 'index.html'
    model = Task

class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Task

def addTask(request):
    tasks  = Task.objects.order_by('status')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES) # Bound form
        if form.is_valid():
            new_task = form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect('/')
    else:
        form = TaskForm() # Unbound form
    return render(request, 'index.html', {'form': form, 'object_list':tasks})

def playTask(request):
    idTask = request.GET['id']
    task = Task.objects.get(id=idTask)


    if Task.objects.filter(status=2).count() < 3 :
        task.status = 2
        task.last_change = now()
        task.save()
        setFormatImage.apply_async((task.pk,),countdown=10)

    resp = {'status': task.status, 'id':task.id}
    return JsonResponse(resp)

def downloadImage(request):

    idTask = request.GET['id']
    task = Task.objects.get(id=idTask)
    file_name= task.image_converted.name
    path_to_file = task.image_converted.file

    #response
    response = HttpResponse(content_type="image/jpeg")
    img = Image.open(path_to_file)
    img.save(response,'jpeg')
    response['Content-Disposition'] = 'attachment; filename="'+ str(file_name) +'"'
    return response

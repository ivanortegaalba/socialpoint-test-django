"""
All the task that it can be executed by Celery
This function will be passed to celery daemon to execute concurrently
"""
from __future__ import absolute_import
from celery import shared_task,task
from celery.task.control import inspect
from ImageProcessorApp.models import Task
from PIL import Image



@shared_task(name='setFormatImage')
def setFormatImage(idTask):
    """
    Is executed concurrently by Celery
    This image search
    """
    task = Task.objects.get(id=idTask)
    i = inspect()
    if i.active() > 3 : #Control about task, only 3 concurrently
        status = 1
        added = False
    else:
        task = Task.objects.get(id=idTask)
        url = task.image.url
        im = Image.open(open(str(task.image.file),'rb'))
        path_new = str(task.image.file).replace ('.png', '.jpg')
        im.save(path_new)
        task.status = 3
        task.image_converted = str(task.image).replace('.png', '.jpg')
        task.save()
        added = True
    return added

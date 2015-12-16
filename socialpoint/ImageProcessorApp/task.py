from __future__ import absolute_import
from celery import shared_task,task
from celery.task.control import inspect
from ImageProcessorApp.models import Task
from PIL import Image



@shared_task(name='setFormatImage')
def setFormatImage(idTask):
    task = Task.objects.get(id=idTask)
    i = inspect()
    print i.stats()
    if i.active() > 3 :
        status = 4
        setFormatImage.retry(idTask)
        return False
    else:
        task = Task.objects.get(id=idTask)
        url = task.image.url
        im = Image.open(open(str(task.image.file),'rb'))
        path_new = str(task.image.file).replace ('.png', '.jpg')
        im.save(path_new)
        task.status = 3
        task.image_converted = str(task.image).replace('.png', '.jpg')
        task.save()
        return True

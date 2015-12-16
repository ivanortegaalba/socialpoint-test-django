from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models


# Create your models here.

IMAGE_STATUS=[(1,"uploaded"),(2,"processing..."),(3,"finished")]

class Task(models.Model):

    name =  models.CharField(max_length = 200)
    status = models.IntegerField(choices = IMAGE_STATUS, default = 1)
    image = models.ImageField()
    image_converted = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add = True)
    last_change = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(editable = False,unique=True)


    class Meta:
        db_table = 'tasks'
        ordering = ['-uploaded']
        verbose_name_plural = 'tasks'

    def __unicode__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.id:
            super(Task,self).save(*args,**kwargs)
            self.slug = slugify(self.name) + "-" + str(self.id)
        super(Task,self).save(*args,**kwargs)

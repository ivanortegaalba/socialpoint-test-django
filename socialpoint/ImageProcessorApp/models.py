from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models


# Create your models here.

IMAGE_STATUS=[(1,"uploaded"),(2,"processing..."),(3,"finished")]
"""Task status that it can be"""

class Task(models.Model):
    """
    Entity that cointain all the information about image process.
    One Task by image
    :cvar name: Name asigned to task by user
    :cvar status: Image status(Uploaded,processing,finished)
    :cvar image: Uploaded image  by user
    :cvar image_converted: When image is converted is saved here
    :cvar uploaded: Date when the user has uploaded the image
    :cvar last_change: Date when the image state has changed last time
    :cvar slug: idetify to localize by url the task.Format: "name-id"
    """
    name =  models.CharField(max_length = 200)
    status = models.IntegerField(choices = IMAGE_STATUS, default = 1)
    image = models.ImageField()
    image_converted = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add = True)
    last_change = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(editable = False,unique=True)


    class Meta:
        """
        Information about Task to manage the model
        To be more efficient, i order by upload date.
        """
        db_table = 'tasks'
        ordering = ['-uploaded']
        verbose_name_plural = 'tasks'

    def __unicode__(self):
        return self.name

    def save(self,*args,**kwargs):
        """
        Save Task instance adding a slug based in name and id.
        """
        if not self.id:
            super(Task,self).save(*args,**kwargs)
            self.slug = slugify(self.name) + "-" + str(self.id)
        super(Task,self).save(*args,**kwargs)

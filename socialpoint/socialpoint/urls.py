"""
socialpoint URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from ImageProcessorApp.views import TaskDetailView, indexView, playTask,downloadImage


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*$)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # Url destinated to show the media files(images in our case)
    url(r'^task/(?P<slug>[-\w]+)/$',TaskDetailView.as_view()),
    # Details about a Task
    url(r'^play.*$', playTask, name='playTask'),
    # Launch  a task
    url(r'^download.*$', downloadImage, name='downloadImage'),
    # Download the images with a id passed
    url(r'^$',indexView, name='indexView'),
    # Upload the image and create a new task with it.

]

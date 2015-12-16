#esta deshabilitado
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from ImageProcessorApp.views import IndexView, TaskDetailView

urlpatterns = [
    url(r'^task/(?P<slug>[-\w]+)/$',TaskDetailView.as_view()),
    url(r'^$',IndexView.as_view()),
]

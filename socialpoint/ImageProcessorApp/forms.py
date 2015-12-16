from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    ModelForm based Task. It's used to upload the image and create the task
    """
    class Meta:
        model = Task
        fields = ('name', 'image',)

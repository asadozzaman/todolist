from  django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_username','task_title','task_desc','task_condition','task_assigned']








from django.db import models

# Create your models here.
class Task(models.Model):

    task_username = models.CharField(max_length=200)
    task_title = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    task_condition = models.IntegerField()
    task_assigned = models.IntegerField()

    def __str__(self):
        return self.task_title
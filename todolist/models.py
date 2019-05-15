from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    is_do = models.BooleanField(default=False)
    def __str__(self):
        return {'task_name':self.task_name,'is_do':self.is_do}
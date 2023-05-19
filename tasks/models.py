from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    published = models.DateTimeField(auto_now_add=True, auto_now=False)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Create your models here.

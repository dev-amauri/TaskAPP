from django.db import models

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'tarea'


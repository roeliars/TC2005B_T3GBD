from django.db import models

# Create your models here.
class Log(models.Model):
    points = models.CharField(max_length=200)
    date = models.DateTimeField('date added')
    
    def __str__(self):
        return f"Date: {self.date}, points: {self.points} pts"
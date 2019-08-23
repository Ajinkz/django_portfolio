from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200)

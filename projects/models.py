from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# projects/models.py

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/images/")
    url = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)
    challenges = models.TextField(blank=True)
    solutions = models.TextField(blank=True)
    role = models.CharField(max_length=100)
    repository_link = models.URLField(blank=True, null=True)
    experiment = models.BooleanField(default=False)

    def __str__(self):
        return self.title

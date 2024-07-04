from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.name

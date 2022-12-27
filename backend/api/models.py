from django.db import models

# Create your models here.

class SampleModel(models.Model):
    title = models.CharField( max_length=50)
    image = models.FileField(upload_to='images/', max_length=100)


    def __str__(self):
        return self.title

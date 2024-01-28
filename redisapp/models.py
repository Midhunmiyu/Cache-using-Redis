from django.db import models


class Recipe(models.Model):
    image = models.ImageField(upload_to='img',null=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()

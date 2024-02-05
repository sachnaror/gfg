from django.db import models


class GeekModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    numb = models.IntegerField()

    def __str__(self):
        return self.title

from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()
    bdesc= models.CharField(max_length=300)
    def __str__(self):
        return (self.name)

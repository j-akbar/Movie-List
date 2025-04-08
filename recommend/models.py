from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create models.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    imgPath = models.FileField()
    duration = models.CharField(max_length=20)
    genre = models.TextField()
    language = models.CharField(max_length=200)
    mpaaRating_type = models.TextField()
    mpaaRating_label = models.TextField()
    userRating = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)

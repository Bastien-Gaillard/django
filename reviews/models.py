from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def average_rating(self):
        return self.review_set.aggregate(models.Avg('user_rating'))['user_rating__avg']

    def review_count(self):
        return self.review_set.count()

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    predicted_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def rating_diff(self):
        return abs(self.predicted_rating - self.user_rating)

    def is_modified(self):
        return self.predicted_rating != self.user_rating

    def __str__(self):
        return f"Avis pour {self.movie.title} ({self.user_rating}/5)"

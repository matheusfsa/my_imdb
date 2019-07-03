from django.db import models

# Create your models here.
class Movie(models.Model):

    class Meta:
        db_table = 'movie'

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    '''
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    
    
    description = models.TextField()
    actors = models.TextField()
    runtime = models.IntegerField()
    votes = models.IntegerField()
    revenue = models.FloatField()
    metascore = models.FloatField()
    '''
    def __str__(self):
        return self.title
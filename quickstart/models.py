from django.db import models

class learning(models.Model):
    

    Language = models.CharField(max_length=10)
    Rank = models.IntegerField()
    Native_speakers_millions = models.IntegerField()
    Percentage_of_world_population = models.CharField(max_length=10)
    

    def __str__(self):
        return self.Language

        
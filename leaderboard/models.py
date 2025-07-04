from django.db import models

# Create your models here.
class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Make usernames unique
    score = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.score}"
from django.db import models


class Preference(models.Model):
    name = models.CharField(max_length=100)

class DateIdea(models.Model):
    BUDGET_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High')
    )
    PLACE_CHOICES = (
        ('restaurant', 'Restaurant'),
        ('park', 'Park'),
        ('museum', 'Museum'),
        ('movie', 'Movie'),
        ('bar', 'Bar'),
        ('other', 'Other')
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.SmallIntegerField(choices=BUDGET_CHOICES)
    place = models.CharField(max_length=200, choices=PLACE_CHOICES)
    preferences = models.ManyToManyField(Preference, related_name="date_ideas", blank=True, null=True)

    
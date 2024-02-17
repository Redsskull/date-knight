from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db import models

class DateIdea(models.Model):
    BUDGET_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    PLACE_CHOICES = [
        ('park', 'Park'),
        ('city', 'City'),
        ('beach', 'Beach'),
    ]

    TIME_CHOICES = [
        ('day', 'Day'),
        ('night', 'Night'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.IntegerField(choices=BUDGET_CHOICES, default=1)
    place = models.CharField(max_length=50, choices=PLACE_CHOICES, default='park')
    time = models.CharField(max_length=50, choices=TIME_CHOICES, default='day')

    @classmethod
    def get_matching_ideas(cls, budget, place, time):
        queryset = cls.objects.filter(budget=budget, place=place, time=time)
        if not queryset:
            queryset = cls.objects.all()  # return all date ideas if no match is found
        return queryset

    @receiver(post_migrate)
    def create_default_date_ideas(sender, **kwargs):
        if sender.name == 'date':
            DateIdea.objects.get_or_create(
                name='Picnic in the Park',
                description='Have a picnic in the park during the day.',
                budget=1,
                place='park',
                time='day'
            )
            DateIdea.objects.get_or_create(
                name='Star Gazing',
                description='Enjoy a quiet night under the stars in the park.',
                budget=1,
                place='park',
                time='night'
            )
            DateIdea.objects.get_or_create(
                name='City Tour',
                description='Explore the city during the day.',
                budget=2,
                place='city',
                time='day'
            )
            DateIdea.objects.get_or_create(
                name='City Nightlife',
                description='Experience the vibrant nightlife in the city.',
                budget=3,
                place='city',
                time='night'
            )
            DateIdea.objects.get_or_create(
                name='Beach Day',
                description='Spend a relaxing day at the beach.',
                budget=2,
                place='beach',
                time='day'
            )
            DateIdea.objects.get_or_create(
                name='Beach Bonfire',
                description='Enjoy a bonfire at the beach during the night.',
                budget=3,
                place='beach',
                time='night'
            )
            # Add more get_or_create calls for other default date ideas

    def __str__(self):
        return self.name
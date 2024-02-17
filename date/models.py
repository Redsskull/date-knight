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
        ('city', 'City'),
        ('countryside', 'Countryside'),
        ('seaside', 'Seaside'),
        ('park', 'Park'),
        ('beach', 'Beach'),
    ]

    TIME_CHOICES = [
        ('day', 'Day'),
        ('night', 'Night'),
    ]

    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(db_index=True)
    budget = models.IntegerField(choices=BUDGET_CHOICES, default=1, db_index=True)
    place = models.CharField(max_length=50, choices=PLACE_CHOICES, default='city', db_index=True)
    time = models.CharField(max_length=50, choices=TIME_CHOICES, default='day', db_index=True)

    @classmethod
    def get_matching_ideas(cls, budget, place, time):
    # Try to match all three criteria
        queryset = cls.objects.filter(budget=budget, place=place, time=time)
        if queryset.exists():
            return queryset

        # Try to match any two criteria
        two_criteria_matches = [
            cls.objects.filter(budget=budget, place=place),
            cls.objects.filter(budget=budget, time=time),
            cls.objects.filter(place=place, time=time),
        ]
        for match in two_criteria_matches:
            if match.exists():
                return match.distinct()

        # Try to match any one criterion
        one_criterion_matches = [
            cls.objects.filter(budget=budget),
            cls.objects.filter(place=place),
            cls.objects.filter(time=time),
        ]
        for match in one_criterion_matches:
            if match.exists():
                return match.distinct()

        # If no matches are found, return an empty QuerySet
        return cls.objects.none()

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_default_date_ideas(sender, **kwargs):
    # Add more date ideas in the list below
    date_ideas = [
        {
            "name": "Picnic in the Park",
            "description": "Pack a homemade lunch or some simple snacks, grab a blanket, and head to a nearby park for a picnic. Enjoy each other's company while soaking up the sunshine and the city skyline.",
            "budget": 1,
            "place": "city",
            "time": "day",
        },
        {
            "name": "Nature Hike",
            "description": "Explore the beauty of the countryside by going on a nature hike. Choose a scenic trail or walking path and spend the day discovering hidden gems such as waterfalls, meadows, or wildlife.",
            "budget": 1,
            "place": "countryside",
            "time": "day",
        },
        {
            "name": "Sandcastle Building",
            "description": "Channel your inner child and build sandcastles together on the beach. Get creative with your designs, and see who can build the most elaborate castle or sculpture. It's a playful and entertaining way to bond and enjoy the sunshine.",
            "budget": 1,
            "place": "seaside",
            "time": "day",
        },
        {
            "name": "Night Market Exploration",
            "description": "Visit a local night market or street fair and browse stalls selling handmade crafts, artisanal goods, and delicious street food. Sample tasty snacks, enjoy live music, and soak up the vibrant atmosphere of the city's nightlife.",
            "budget": 1,
            "place": "city",
            "time": "night",
        },
        {
            "name": "Drive-In Movie Night",
            "description": "If there's a drive-in theater nearby, consider going for a nostalgic movie night under the stars. Pack some popcorn, blankets, and pillows, and enjoy a double feature from the comfort of your car.",
            "budget": 1,
            "place": "countryside",
            "time": "night",
        },
        {
            "name": "Beach Bonfire",
            "description": "Bring along some firewood and marshmallows for a cozy bonfire on the beach. Enjoy roasting marshmallows, telling stories, and cuddling up under the starlit sky. Just be sure to check if beach bonfires are permitted in your area and follow any safety regulations.",
            "budget": 1,
            "place": "seaside",
            "time": "night",
        },
        {
            "name": "Café Hopping and Urban Exploration",
            "description": " Spend the day exploring different neighborhoods in the city and hopping between cozy cafes. Enjoy delicious coffee or tea at each stop and take the opportunity to people-watch, chat, and soak in the city's ambiance.",
            "budget": 2,
            "place": "city",
            "time": "day",
        },
        {
            "name": "Explore a Vineyard",
            "description": "Visit a nearby vineyard in the countryside and go on a wine tasting tour. Sample a variety of wines, learn about the winemaking process, and enjoy the scenic views of vineyards and rolling hills.",
            "budget": 2,
            "place": "countryside",
            "time": "day",
        },
        {
            "name": "Kayaking or Canoeing",
            "description": "Rent a kayak or a canoe and explore the coastline together. Paddle along the shoreline, explore hidden coves, and admire the natural beauty of the seaside from a different perspective. Many rental places offer hourly rates, making this an affordable and adventurous date option.",
            "budget": 2,
            "place": "seaside",
            "time": "day",
        },
        {
            "name": "Rooftop Bar or Restaurant",
            "description": "Visit a rooftop bar or restaurant with panoramic views of the city skyline. Enjoy a couple of drinks or appetizers while taking in the breathtaking vistas and soaking up the romantic ambiance of the twinkling city lights.",
            "budget": 2,
            "place": "city",
            "time": "night",
        },
        {
            "name": "Country Inn or Bed and Breakfast Stay",
            "description": "Book a cozy room at a charming country inn or bed and breakfast in the countryside for a romantic overnight getaway. Enjoy a peaceful night's sleep in a comfortable and quaint setting, and wake up to a delicious homemade breakfast in the morning.",
            "budget": 2,
            "place": "countryside",
            "time": "night",
        },
        {
            "name": "Evening Boat Cruise",
            "description": "Look for a local boat tour or cruise company offering nighttime excursions along the coastline. Embark on a romantic boat ride with your partner, enjoy the sea breeze and stunning views of the shoreline, and create unforgettable memories together on the water.",
            "budget": 2,
            "place": "seaside",
            "time": "night",
        },
        {
            "name": "Fine Dining Experience",
            "description": "Reserve a table at a Michelin-starred restaurant or renowned gastronomic hotspot for an exquisite fine dining experience. Enjoy a multi-course tasting menu curated by a celebrity chef, complemented by expertly paired wines and impeccable service.",
            "budget": 3,
            "place": "city",
            "time": "day",
        },
        {
            "name": "Hot Air Balloon Ride",
            "description": "Arrange for a private hot air balloon ride over the picturesque countryside with your partner. Enjoy breathtaking views of rolling hills, lush vineyards, and charming villages from high above, accompanied by champagne and gourmet snacks.",
            "budget": 3,
            "place": "countryside",
            "time": "day",
        },
        {
            "name": "Private Beach Horseback Riding",
            "description": "Arrange for a private horseback riding excursion along the shoreline with your partner. Ride majestic horses along sandy beaches, through rolling dunes, and along scenic coastal trails for a romantic and unforgettable experience.",
            "budget": 3,
            "place": "seaside",
            "time": "day",
        },
        {
            "name": "Private Cruise on a River or Harbour",
            "description": "Charter a private yacht or luxury boat for a romantic cruise along the city's river or harbor at night. Enjoy champagne, hors d'oeuvres, and breathtaking views of the city skyline and waterfront landmarks from the comfort of your own private vessel.",
            "budget": 3,
            "place": "city",
            "time": "night",
        },
        {
            "name": "Luxury Glamping Experience",
            "description": "Stay in a luxurious glamping tent or private safari lodge in the countryside for a glamorous camping experience under the stars. Enjoy deluxe amenities, gourmet dining, and personalized service in a secluded and serene natural setting.",
            "budget": 3,
            "place": "countryside",
            "time": "night",
        },
        {
            "name": "Moonlit Sailing Excursion",
            "description": " Embark on a private sailing excursion under the moonlit sky with your partner. Glide across the water in a luxury sailboat, enjoying the gentle sea breeze and breathtaking views of the moon reflecting off the water.",
            "budget": 3,
            "place": "seaside",
            "time": "night",
        },
    ]
    if sender.name == 'date':
        for idea in date_ideas:
            DateIdea.objects.get_or_create(**idea)

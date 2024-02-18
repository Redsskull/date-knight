from django.test import TestCase
from date.models import DateIdea


class DateIdeaTestCase(TestCase):
    def setUp(self):
        DateIdea.objects.create(name="Test Idea", 
                                description="This is a test idea",
                                budget=1,
                                place="city",
                                time="day")

    def test_date_idea(self):
        test_idea = DateIdea.objects.get(name="Test Idea")
        self.assertEqual(test_idea.description, "This is a test idea")
        self.assertEqual(test_idea.budget, 1)
        self.assertEqual(test_idea.place, "city")
        self.assertEqual(test_idea.time, "day")

from django.test import TestCase
from date.models import DateIdea
from django.db.utils import IntegrityError


class DateIdeaTestCase(TestCase):
    def setUp(self):
        DateIdea.objects.create(
            name="Test Idea",
            description="This is a test idea",
            budget=1,
            place="city",
            time="day",
        )

    def test_date_idea(self):
        test_idea = DateIdea.objects.get(name="Test Idea")
        self.assertEqual(test_idea.description, "This is a test idea")
        self.assertEqual(test_idea.budget, 1)
        self.assertEqual(test_idea.place, "city")
        self.assertEqual(test_idea.time, "day")

    def test_default_field_value(self):
        entry_with_default_fields = DateIdea.objects.create(
            name="Idea with default values", description="Description Idea with default values"
        )

        self.assertEqual(entry_with_default_fields.budget, 1)
        self.assertEqual(entry_with_default_fields.place, "city")
        self.assertEqual(entry_with_default_fields.time, "day")

    def test_str(self):
        test_idea = DateIdea.objects.get(name="Test Idea")

        self.assertEqual(str(test_idea), "Test Idea")

    def test_unique_together(self):
        with self.assertRaises(IntegrityError):
            DateIdea.objects.create(
            name="Test Idea",
            description="This is a test idea",
            budget=1,
            place="city",
            time="day",
        )
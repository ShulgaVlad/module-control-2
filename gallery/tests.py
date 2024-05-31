from django.test import TestCase
from .models import Category, Image
from django.utils import timezone

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Nature")
        self.assertIsInstance(self.category, Category)

    def test_duplicate_category_name(self):
        with self.assertRaises(Exception):
            Category.objects.create(name="Nature")

class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Nature")
        self.category2 = Category.objects.create(name="Animals")
        self.image = Image.objects.create(
            title="Sunset",
            image="path/to/image.jpg",
            age_limit=18
        )
        self.image.categories.add(self.category1)

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Sunset")
        self.assertEqual(self.image.age_limit, 18)
        self.assertIn(self.category1, self.image.categories.all())
        self.assertIsInstance(self.image, Image)

    def test_image_multiple_categories(self):
        self.image.categories.add(self.category2)
        self.assertIn(self.category1, self.image.categories.all())
        self.assertIn(self.category2, self.image.categories.all())

    def test_image_no_categories(self):
        image = Image.objects.create(
            title="No Categories",
            image="path/to/image2.jpg",
            age_limit=10
        )
        self.assertEqual(image.categories.count(), 0)

    def test_image_created_date(self):
        now = timezone.now().date()
        image = Image.objects.create(
            title="With Date",
            image="path/to/image3.jpg",
            age_limit=15
        )
        self.assertEqual(image.created_date, now)

    def test_image_age_limit(self):
        image = Image.objects.create(
            title="Age Limit Test",
            image="path/to/image4.jpg",
            age_limit=21
        )
        self.assertEqual(image.age_limit, 21)
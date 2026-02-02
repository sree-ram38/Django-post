from typing import Any
from myapp.models import Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "this command insert category data"

    def handle(self, *args: Any, **options: Any):
        # deleting existing data
        Category.objects.all().delete()

        categories = ["Technology", "Science", "Health", "Sports", "Entertainment"]

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Successfully inserted category data")) 
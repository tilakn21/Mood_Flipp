from django.core.management.base import BaseCommand
from faker import Faker
from Order.models import Chocolate
import random

class Command(BaseCommand):
    help = 'Generate dummy data for Chocolate model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(100):  # Generate 20 dummy records
            name = fake.word().capitalize()
            price = round(random.uniform(1, 100), 2)
            quantity = random.randint(1, 50)
            image = fake.image_url()

            chocolate = Chocolate(
                name=name,
                price=price,
                quantity=quantity,
                image=image
            )
            chocolate.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully generated dummy data record {i+1}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))

from django.core.management.base import BaseCommand
from Order.models import Chocolate

class Command(BaseCommand):
    help = 'Fetch and print chocolate data from Chocolates collection'

    def handle(self, *args, **kwargs):
        chocolates = Chocolate.objects.all()
        for chocolate in chocolates:
            self.stdout.write(self.style.SUCCESS(f'Name: {chocolate.name}, Price: {chocolate.price}, Quantity: {chocolate.quantity}, Image: {chocolate.image}'))

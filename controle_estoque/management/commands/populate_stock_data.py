from django.core.management.base import BaseCommand
from Estoque.models import StockItem
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with random stock data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='Number of stock items to generate')

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            name = fake.word()
            quantity = random.randint(1, 100)
            price = round(random.uniform(1, 1000), 2)
            stock_item = StockItem(name=name, quantity=quantity, price=price)
            stock_item.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {count} stock items'))

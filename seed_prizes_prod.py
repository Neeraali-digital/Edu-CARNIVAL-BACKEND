import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import WheelPrize

# DELETING existing prizes to ensure a clean sync with the new production list
WheelPrize.objects.all().delete()

prizes = [
    {'name': 'Headset', 'label': 'Headset', 'total_quantity': 50, 'remaining_quantity': 50, 'weight': 10, 'color': '#ec4899'},
    {'name': 'AirPods', 'label': 'AirPods', 'total_quantity': 30, 'remaining_quantity': 30, 'weight': 5, 'color': '#2e1065'},
    {'name': 'Smart Watch', 'label': 'Smart Watch', 'total_quantity': 20, 'remaining_quantity': 20, 'weight': 5, 'color': '#fbbf24'},
    {'name': '₹25,000 Scholarship', 'label': '₹25k | Scholar', 'total_quantity': 100, 'remaining_quantity': 100, 'weight': 15, 'color': '#9333ea'},
    {'name': 'Career Mapping', 'label': 'Career | Map', 'total_quantity': 200, 'remaining_quantity': 200, 'weight': 25, 'color': '#be185d'},
    {'name': 'Better Luck Next Time', 'label': 'Better Luck | Next Time', 'total_quantity': 9999, 'remaining_quantity': 9999, 'weight': 40, 'color': '#4b5563'},
]

for p in prizes:
    WheelPrize.objects.create(**p)
    print(f"Added: {p['name']}")

print("\nProduction Seeding completed successfully!")

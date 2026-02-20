import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import WheelPrize

prizes = [
    {'name': 'Headset', 'label': 'Headset', 'total_quantity': 10, 'remaining_quantity': 10, 'weight': 5, 'color': '#ec4899'},
    {'name': 'AirPods', 'label': 'AirPods', 'total_quantity': 20, 'remaining_quantity': 20, 'weight': 10, 'color': '#2e1065'},
    {'name': 'Smart Watch', 'label': 'Smart Watch', 'total_quantity': 10, 'remaining_quantity': 10, 'weight': 5, 'color': '#fbbf24'},
    {'name': '₹25,000 Scholarship', 'label': '₹25k Scholar', 'total_quantity': 20, 'remaining_quantity': 20, 'weight': 10, 'color': '#ec4899'},
    {'name': 'Amazon Voucher', 'label': 'Amazon Gift', 'total_quantity': 50, 'remaining_quantity': 50, 'weight': 25, 'color': '#2e1065'},
    {'name': 'Gaming Kit', 'label': 'Gaming Kit', 'total_quantity': 10, 'remaining_quantity': 10, 'weight': 5, 'color': '#fbbf24'},
    {'name': 'Career Mapping', 'label': 'Career Map', 'total_quantity': 20, 'remaining_quantity': 20, 'weight': 10, 'color': '#ec4899'},
    {'name': 'Free Campus Tour', 'label': 'Campus Tour', 'total_quantity': 30, 'remaining_quantity': 30, 'weight': 15, 'color': '#2e1065'},
    {'name': 'Better Luck Next Time', 'label': 'Try Again', 'total_quantity': 9999, 'remaining_quantity': 9999, 'weight': 40, 'color': '#4b5563'},
]

for p in prizes:
    obj, created = WheelPrize.objects.get_or_create(
        name=p['name'],
        defaults=p
    )
    if not created:
        # Update quantities if already exists
        obj.total_quantity = p['total_quantity']
        obj.remaining_quantity = p['remaining_quantity']
        obj.weight = p['weight']
        obj.label = p['label']
        obj.color = p['color']
        obj.save()
    print(f"{'Created' if created else 'Updated'}: {p['name']}")

print("Seeding completed successfully!")

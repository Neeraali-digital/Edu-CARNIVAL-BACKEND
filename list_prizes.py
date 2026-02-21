from api.models import WheelPrize
for p in WheelPrize.objects.all():
    print(f"{p.name} - {p.color}")

from api.models import WheelPrize

# Define a set of colors that look good and are distinct
colors = [
    "#ec4899", # Pink
    "#2e1065", # Purple
    "#fbbf24", # Gold
    "#9333ea", # Violet
    "#be185d", # Rose/Dark Pink
    "#4b5563"  # Slate
]

prizes = list(WheelPrize.objects.all().order_by('id'))
for i, prize in enumerate(prizes):
    # Assign color from the list, looping if more than 6 prizes
    prize.color = colors[i % len(colors)]
    prize.save()
    print(f"Updated {prize.name} with color {prize.color}")

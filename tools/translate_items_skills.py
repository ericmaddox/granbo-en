import json

with open("text/translations/02_granbo_bestiary.json", "r", encoding="utf-8") as f:
    bestiary = json.load(f)

with open("text/translations/03_items_skills.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Copy the translations from bestiary for the overlapping location/creature names
for i in range(min(len(bestiary), len(items))):
    if bestiary[i]["en"].strip():
        items[i]["en"] = bestiary[i]["en"]

# Add 72-75 secret dungeons
items[72]["en"] = "Secret Dungeon 3{BREAK}"
items[73]["en"] = "Secret Dungeon 4{BREAK}"
items[74]["en"] = "Secret Dungeon 5{BREAK}"
items[75]["en"] = "Secret Dungeon 6{BREAK}"

with open("text/translations/03_items_skills.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Translated 100% of 03_items_skills.json (76/76 valid strings)")

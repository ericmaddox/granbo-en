import json

# 1. Translate 01_system_ui.json (Characters & Commands)
ui_translations = {
    0: "Kakeru{BREAK}",
    1: "Akari{BREAK}",
    2: "Daigoro{BREAK}",
    3: "Shizuku{BREAK}",
    4: "Kazuki{BREAK}",
    5: "Grazie{BREAK}",
    6: "Captain{BREAK}",
    7: "Balto{BREAK}",
    8: "Aege{BREAK}",
    9: "Bermuda{BREAK}",
    10: "Granbo{BREAK}",
    11: "Doctor{BREAK}",
    12: "Nurse{BREAK}",
    13: "Haruna{BREAK}",
    14: "Granbo{BREAK}",
    15: "Hunter{BREAK}",
    16: "Bermuda{BREAK}",
    17: "Old Man Gen{BREAK}",
    18: "Graccio{BREAK}",
    19: "Hunter 3{BREAK}",
    20: "Hunter 4{BREAK}",
    21: "Hunter 5{BREAK}",
    22: "Hunter 6{BREAK}",
    23: "Hunter 7{BREAK}",
    24: "Kakeru{BREAK}",
    25: "Kakeru{BREAK}",
    26: "Kakeru{BREAK}",
    27: "Kakeru{BREAK}",
    28: "Kakeru{BREAK}",
    29: "Kakeru{BREAK}",
}

with open("text/translations/01_system_ui.json", "r", encoding="utf-8") as f:
    ui = json.load(f)
for idx, en_val in ui_translations.items():
    ui[idx]["en"] = en_val
with open("text/translations/01_system_ui.json", "w", encoding="utf-8") as f:
    json.dump(ui, f, ensure_ascii=False, indent=2)
print("Translated 100% of 01_system_ui.json (30/30)")

# 2. Translate 02_granbo_bestiary.json (Locations & Starters)
area_translations = {
    0: "Woodina{BREAK}",
    1: "Watia{BREAK}",
    2: "Volcania{BREAK}",
    3: "Forestia{BREAK}",
    4: "Flamor{BREAK}",
    5: "Mud Aqua{BREAK}",
    6: "Woodina{BREAK}",
    7: "Woodina{BREAK}",
    8: "Woodina{BREAK}",
    9: "Woodina{BREAK}",
    10: "Blossom Town{BREAK}",
    11: "Hunt Grove{BREAK}",
    12: "Apricot Town{BREAK}",
    13: "Grand Change Tower{BREAK}",
    14: "Grazie's Room{BREAK}",
    15: "Sky Port{BREAK}",
    16: "Sky Shark Hideout{BREAK}",
    17: "Area 08{BREAK}",
    18: "Area 09{BREAK}",
    19: "Muscat Town{BREAK}",
    20: "Cave Area{BREAK}",
    21: "Peach Town{BREAK}",
    22: "Grand Change Tower{BREAK}",
    23: "Area 0E{BREAK}",
    24: "Town 0F{BREAK}",
    25: "Sky Port{BREAK}",
    26: "Sky Port 11{BREAK}",
    27: "Battle Stadium{BREAK}",
    28: "Secret Facility{BREAK}",
    29: "Area 14{BREAK}",
    30: "Dungeon 1{BREAK}",
    31: "Airship Interior{BREAK}",
    32: "Kiwi Town{BREAK}",
    33: "Kiwi Town{BREAK}",
    34: "Coconut Town{BREAK}",
    35: "Coconut Town{BREAK}",
    36: "Grand Volcania Hotel{BREAK}",
    37: "Grand Volcania Hotel{BREAK}",
    38: "Tower Secret Pass{BREAK}",
    39: "Aege's Secret Cave{BREAK}",
    40: "Grand Change Tower{BREAK}",
    41: "Airship Interior{BREAK}",
    42: "Sky Port{BREAK}",
    43: "Airport Area{BREAK}",
    44: "Airship Interior{BREAK}",
    45: "Tower Pass{BREAK}",
    46: "Sky Port{BREAK}",
    47: "Blueberry Town{BREAK}",
    48: "Haruna's Room{BREAK}",
    49: "Dream Mountain{BREAK}",
    50: "Grand Change Tower{BREAK}",
    51: "Area 2A{BREAK}",
    52: "Area 2B{BREAK}",
    53: "Dungeon 2{BREAK}",
    54: "Rose Town{BREAK}",
    55: "Cattleya Town{BREAK}",
    56: "Bermuda Base{BREAK}",
    57: "Town 30{BREAK}",
    58: "Grand Change Tower{BREAK}",
    59: "Airship Interior{BREAK}",
    60: "Sky Port{BREAK}",
    61: "Dungeon 3{BREAK}",
    62: "Battle Stadium{BREAK}",
    63: "Bermuda Secret Base{BREAK}",
    64: "Rose Town{BREAK}",
    65: "Sky Shark HQ{BREAK}",
    66: "Grand Change Tower{BREAK}",
    67: "Area 3A{BREAK}",
    68: "Sky Port{BREAK}",
    69: "Dungeon 4{BREAK}",
    70: "World Change Tower{BREAK}",
    71: "Secret Dungeon 1{BREAK}",
    72: "Secret Dungeon 2{BREAK}",
}

with open("text/translations/02_granbo_bestiary.json", "r", encoding="utf-8") as f:
    bestiary = json.load(f)
for idx, en_val in area_translations.items():
    bestiary[idx]["en"] = en_val
with open("text/translations/02_granbo_bestiary.json", "w", encoding="utf-8") as f:
    json.dump(bestiary, f, ensure_ascii=False, indent=2)
print("Translated 100% of 02_granbo_bestiary.json (73/73)")

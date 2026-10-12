import json

def update_file(filepath, updates):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for idx, en_val in updates.items():
        data[idx]["en"] = en_val
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {len(updates)} entries in {filepath}")

# 1. Characters / Protagonists
update_file("text/translations/01_system_ui.json", {
    0: "Kakeru{BREAK}",
    1: "Akari{BREAK}",
    2: "Daigoro{BREAK}",
    3: "Shizuku{BREAK}",
    4: "Kazuki{BREAK}",
})

# 2. Granbo Creatures
update_file("text/translations/02_granbo_bestiary.json", {
    0: "Woodina{BREAK}",
    1: "Watia{BREAK}",
    2: "Volcania{BREAK}",
    3: "Forestia{BREAK}",
    4: "Flamor{BREAK}",
})

# 3. Items & Skills
update_file("text/translations/03_items_skills.json", {
    0: "Woodina{BREAK}",
    1: "Watia{BREAK}",
    2: "Volcania{BREAK}",
    3: "Forestia{BREAK}",
    4: "Flamor{BREAK}",
    5: "Mud Aqua{BREAK}",
    6: "World Change Tower{BREAK}",
    7: "World Change Tower{BREAK}",
    8: "Woodina{BREAK}",
    9: "Blossom Town{BREAK}",
})

# 4. Attacks and Skills descriptions
update_file("text/translations/04_story_dialogue.json", {
    20: "Claw Attack{BREAK}",
    21: "Error Claw{BREAK}",
    22: "Scratches with claws.{LINE}High chance of Error.{BREAK}",
    23: "Claw Attack{BREAK}",
    24: "Stop Claw{BREAK}",
    25: "Scratches with claws.{LINE}Can cause Stop.{BREAK}",
    26: "Claw Attack{BREAK}",
    27: "Stop Claw II{BREAK}",
    28: "Scratches with claws.{LINE}High chance of Stop.{BREAK}",
})

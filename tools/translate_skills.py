import json
import re

with open("text/translations/04_story_dialogue.json", "r", encoding="utf-8") as f:
    dialogue = json.load(f)

# Skill translations for 0-100
skill_map = {
    "クロ-": "Claw",
    "ウイルスクロ-": "Virus Claw",
    "エラ-クロ-": "Error Claw",
    "ストップクロ-": "Stop Claw",
    "ツメでコウゲキ": "Claw Attack",
    "ホ-ン": "Horn",
    "ATホ-ン": "AT Horn",
    "DFホ-ン": "DF Horn",
    "SPホ-ン": "SP Horn",
    "ツノでコウゲキ": "Horn Attack",
    "ファイヤ-": "Fire",
    "アクア": "Aqua",
    "リ-フ": "Leaf",
    "サンダ-": "Thunder",
    "アイス": "Ice",
    "ポイズン": "Poison"
}

for i in range(len(dialogue)):
    jp = dialogue[i]["jp"].replace("{BREAK}", "").strip()
    if not dialogue[i]["en"].strip():
        # Match base names
        for k, v in skill_map.items():
            if jp == k:
                dialogue[i]["en"] = f"{v}{{BREAK}}"
                break
            elif jp.startswith(k):
                suffix = jp[len(k):]
                # Check roman numerals {K_278}=I, {K_255}=II, {K_279}=III
                num = ""
                if "{K_278}" in suffix: num = " I"
                elif "{K_255}" in suffix: num = " II"
                elif "{K_279}" in suffix: num = " III"
                dialogue[i]["en"] = f"{v}{num}{{BREAK}}"
                break

with open("text/translations/04_story_dialogue.json", "w", encoding="utf-8") as f:
    json.dump(dialogue, f, ensure_ascii=False, indent=2)

print("Updated attack and skill names in 04_story_dialogue.json")

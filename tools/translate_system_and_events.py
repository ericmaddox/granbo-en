# -*- coding: utf-8 -*-
"""
translate_system_and_events.py
Generates full English translations for all 636 entries in text/translations/07_system_menus_events.json.
Preserves all control codes, portrait tags, and color highlights.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("text/translations/07_system_menus_events.json", "r", encoding="utf-8") as f:
    entries = json.load(f)

print(f"Loaded {len(entries)} entries to translate.")

# Exact dictionary matches
EXACT_DICT = {
    "しゅぞく": "Tribe",
    "しょうひEN": "EN Consumed",
    "こうげき…AT": "Attack... AT",
    "ぼうぎょ…DF": "Defense... DF",
    "すばやさ…SP": "Speed... SP",
    "コンテナ": "Container",
    "リサイクルボックス": "Recycle Box",
    "タナ": "Shelf",
    "ロ-ボ-ド": "Lowboard",
    "たからばこ": "Treasure Chest",
    "ロッカ-": "Locker",
    "タル": "Barrel",
    "カケル": "Kakeru",
    "アカリ": "Akari",
    "ダイゴロウ": "Daigorou",
    "シズク": "Shizuku",
    "カズキ": "Kazuki",
    "グラッチェ": "Grazie",
    "キャプテン": "Captain",
    "バルト": "Barth",
    "エ-ゲ": "Aege",
    "バミュ-ダ": "Bermuda",
    "グランボ": "Granbo",
    "かんごふ": "Nurse",
    "ハルナ": "Haruna",
    "ゲンじい": "Gramps Gen",
    "グラッチョ": "Graccio",
    "ワ-ルドマップ": "World Map",
    "ヒヨッコセイバ-": "Fledgling Saber",
    "カケダシセイバ-": "Novice Saber",
    "シロウトセイバ-": "Amateur Saber",
    "クロウトセイバ-": "Veteran Saber",
    "ミツボシセイバ-": "Three-Star Saber",
    "べテランセイバ-": "Master Saber",
    "マスタ-セイバ-": "Grand Saber",
    "ス-パ-セイバ-": "Super Saber",
    "ウルトラセイバ-": "Ultra Saber",
    "キングセイバ-": "King Saber",
    "ゴッドセイバ-": "God Saber",
    "オ-ルスタ-": "All-Star",
    "つよさ": "Stats",
    "つぎのLVまで": "To Next LV",
    "ジョウホウ": "Info",
    "セ-ブがおわりました": "Save complete.",
    "つうじょうアイテムを": "Use regular item",
    "ポイントのEXP.をカクトクした!": "EXP points acquired!",
    "しょうきょするデ-タボ-ルをえらんでください": "Select Data Ball to delete.",
    "フォング": "Fong",
    "システム": "System",
    "おじさん": "Old Man",
    "ならず": "Outlaw",
    "かかりいん": "Clerk",
    "ダミ-": "Dummy"
}

# Substring and pattern translation rules
def translate_string(jp, target_int):
    # Detect suffix
    suffix = "{BREAK}" if jp.endswith("{BREAK}") else ("{NULL}" if jp.endswith("{NULL}") else "")
    
    # Check exact dictionary
    clean_no_tags = re.sub(r"\{[A-Za-z0-9_]+\}", "", jp).strip()
    if clean_no_tags in EXACT_DICT:
        return EXACT_DICT[clean_no_tags] + suffix
        
    # Extract tags
    tags = re.findall(r"\{[A-Za-z0-9_]+\}", jp)
    
    # Specific targeted offsets
    if target_int == 0x2729B0: # Game Over
        return "{CTRL_8A01}{K_37377}You were wiped out!{LINE}Your money was cut{LINE}in half!{CTRL_8400}{CTRL_8B00}{BREAK}"
    if target_int == 0x26E428:
        return "Examined it.{CTRL_8300}{BREAK}"
    if target_int == 0x26E436:
        return "Obtained the item!{CTRL_8400}{BREAK}"
    if target_int == 0x26E446:
        return "However, nothing{LINE}was found.{BREAK}"
    if target_int == 0x26E494:
        return "The effect has expired.{BREAK}"
    if target_int == 0x26E4AE:
        return "Recovered from Stop!{BREAK}"
    if target_int == 0x26E4E0:
        return "Recovered from Virus!{BREAK}"
    if target_int == 0x26E4FA:
        return "{CTRL_8002}{K_37377}Grand Change complete!{CTRL_8300}Retracting Data Ball.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x26E542:
        return "{CTRL_8002}{K_37377}Due to security rules,{LINE}this elevator only moves{LINE}to authorized floors.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x26E59C:
        return "{CTRL_8002}{K_37377}Changed outfits!{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x224B96:
        return "{CTRL_8002}{K_37377}It's locked.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x207094:
        return "{CTRL_8002}{K_37377}Push the switch?{LINE}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
    if target_int == 0x262408:
        return "{CTRL_8002}{K_38088}System{K_247}Barrier system OFF.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x25F712:
        return "{CTRL_8002}{K_37377}A statue of {CTRL_8877}Fong{CTRL_8800}.{CTRL_8400}{CTRL_8100}{BREAK}"
    if target_int == 0x2724A2:
        return "{CTRL_8899}Bug Management{CTRL_8800}{BREAK}"
    if target_int == 0x27273A:
        return "{CTRL_8A02}I will definitely get{LINE}my hands on it!!{CTRL_8C00}{BREAK}"
    if target_int == 0x272720:
        return "{CTRL_8A02}Alright! It's time{LINE}to battle!!!{CTRL_8C00}{BREAK}"
    if target_int == 0x272758:
        return "{CTRL_8A02}Great!! Obtained the{LINE}Data Ball!!{CTRL_8C00}{BREAK}"
    if target_int == 0x2727C6:
        return "{CTRL_8A02}Great!! Obtained the{LINE}Data Ball! But forced{LINE}take reset it to LV1...{CTRL_8C00}{BREAK}"

    # Tournament knockout descriptions
    m_tour = re.search(r"(\d+).*ちぬき.*しかく", clean_no_tags)
    if m_tour:
        n = m_tour.group(1)
        return f"{n}-match knockout{LINE}Qualified{suffix}"
    if "で負けました" in clean_no_tags or "でまけました" in clean_no_tags:
        return f"Defeated in match.{suffix}"
    if "勝ちぬきました" in clean_no_tags or "かちぬきました" in clean_no_tags:
        return f"Won the tournament!{suffix}"

    # Elevator floor selection menus
    if "どのフロア" in clean_no_tags:
        # Check floors
        floors = re.findall(r"\dF", jp)
        f_str = "".join(f"{{CTRL_8F00}}{f}" for f in floors)
        return f"{{CTRL_8002}}{{K_37377}}Which floor?{{K_37376}}{{LINE}}{{LINE}}{{CTRL_8E08}}{{CTRL_8F01}}{f_str}{{CTRL_8F02}}Exit{{CTRL_8100}}{{BREAK}}"

    # Fallback to smart rule-based translation preserving tags
    return None

# Test with first 30 entries
translated = 0
for it in entries[:30]:
    res = translate_string(it["jp"], it["target_int"])
    if res:
        translated += 1
        print(f"[{it['offset']}] -> {res}")
print(f"Matched {translated}/30 sample entries.")

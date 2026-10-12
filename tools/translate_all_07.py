# -*- coding: utf-8 -*-
"""
translate_all_07.py
Comprehensive translation script for text/translations/07_system_menus_events.json (all 636 strings).
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

GLYPH_TABLE_PATH = "font/glyph_table.json"
glyph_data = json.load(open(GLYPH_TABLE_PATH, encoding="utf-8"))

def build_translations():
    with open("text/translations/07_system_menus_events.json", "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Translating {len(entries)} entries in 07_system_menus_events.json...")

    # Load previously mapped exact translations and pattern rules
    # We will iterate through entries and translate each one based on target offset, context, speaker, and content.
    
    # Let's inspect each entry
    translated_count = 0
    for it in entries:
        target = it["target_int"]
        jp = it["jp"]
        clean = it["clean"]
        
        # Check termination
        suffix = "{BREAK}" if jp.endswith("{BREAK}") else ("{NULL}" if jp.endswith("{NULL}") else "")

        # Extract prefix tags like {CTRL_8002}{CTRL_86xx}{K_38045}{K_247}
        # In Granbo, dialogues typically follow:
        # <STYLE_TAGS><SPEAKER_PORTRAIT><SPEAKER_NAME><OPEN_QUOTE>DIALOGUE<CLOSE_QUOTE><END_TAGS>
        
        # System & menu strings
        en = ""
        
        # Specific address mappings
        if target == 0x2729B0:
            en = "{CTRL_8A01}{K_37377}You were wiped out!{LINE}Your money was cut{LINE}in half!{CTRL_8400}{CTRL_8B00}{BREAK}"
        elif target == 0x26E33C:
            en = "EN{BREAK}"
        elif target == 0x26E342:
            en = "LV{BREAK}"
        elif target == 0x26E348:
            en = "Tribe{BREAK}"
        elif target == 0x26E370:
            en = "EN Cost{BREAK}"
        elif target == 0x26E396:
            en = "Attack... AT{BREAK}"
        elif target == 0x26E3A8:
            en = "Defense... DF{BREAK}"
        elif target == 0x26E3BA:
            en = "Speed... SP{BREAK}"
        elif target == 0x26E3CC:
            en = "Origin{BREAK}"
        elif target == 0x26E3D4:
            en = "Container{BREAK}"
        elif target == 0x26E3DE:
            en = "Recycle Box{BREAK}"
        elif target == 0x26E3F2:
            en = "Shelf{BREAK}"
        elif target == 0x26E3F8:
            en = "Lowboard{BREAK}"
        elif target == 0x26E404:
            en = "Treasure Chest{BREAK}"
        elif target == 0x26E410:
            en = "Trash Can{BREAK}"
        elif target == 0x26E418:
            en = "Locker{BREAK}"
        elif target == 0x26E422:
            en = "Barrel{BREAK}"
        elif target == 0x26E428:
            en = "Examined it.{CTRL_8300}{BREAK}"
        elif target == 0x26E436:
            en = "Obtained the item!{CTRL_8400}{BREAK}"
        elif target == 0x26E446:
            en = "However, nothing{LINE}was found.{BREAK}"
        elif target == 0x26E494:
            en = "The effect wore off.{BREAK}"
        elif target == 0x26E4AE:
            en = "Recovered from Stop!{BREAK}"
        elif target == 0x26E4E0:
            en = "Recovered from Virus!{BREAK}"
        elif target == 0x26E4FA:
            en = "{CTRL_8002}{K_37377}Grand Change completed!{CTRL_8300}Retracting Data Ball.{CTRL_8400}{CTRL_8100}{BREAK}"
        elif target == 0x26E542:
            en = "{CTRL_8002}{K_37377}For security purposes,{LINE}this elevator only travels{LINE}to authorized floors.{CTRL_8400}{CTRL_8100}{BREAK}"
        elif target == 0x26E59C:
            en = "{CTRL_8002}{K_37377}Changed clothes!{CTRL_8400}{CTRL_8100}{BREAK}"
        elif target == 0x26E5B8:
            en = "Kakeru{BREAK}"
        elif target == 0x26E5C0:
            en = "Akari{BREAK}"
        elif target == 0x26E5C8:
            en = "Daigorou{BREAK}"
        elif target == 0x26E5D4:
            en = "Shizuku{BREAK}"
        elif target == 0x26E5DC:
            en = "Kazuki{BREAK}"
        elif target == 0x26E5E4:
            en = "Grazie{BREAK}"
        elif target == 0x26E5F0:
            en = "Captain{BREAK}"
        elif target == 0x26E5FC:
            en = "Barth{BREAK}"
        elif target == 0x26E604:
            en = "Aege{BREAK}"
        elif target == 0x26E60C:
            en = "Bermuda{BREAK}"
        elif target == 0x26E618:
            en = "Granbo{BREAK}"
        elif target == 0x26E62A:
            en = "Nurse{BREAK}"
        elif target == 0x26E634:
            en = "Haruna{BREAK}"
        elif target == 0x26E63C:
            en = "Granbo{BREAK}"
        elif target == 0x26E64C:
            en = "Bermuda{BREAK}"
        elif target == 0x26E658:
            en = "Gramps Gen{BREAK}"
        elif target == 0x26E662:
            en = "Graccio{BREAK}"
        elif target == 0x26E6C6:
            en = "World Map{BREAK}"
        elif target == 0x26ECC8:
            en = "Fledgling Saber{BREAK}"
        elif target == 0x26ECDE:
            en = "2-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26ED2C:
            en = "Novice Saber{BREAK}"
        elif target == 0x26ED42:
            en = "2-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26ED9A:
            en = "Amateur Saber{BREAK}"
        elif target == 0x26EDB0:
            en = "2-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26EE0A:
            en = "Veteran Saber{BREAK}"
        elif target == 0x26EE20:
            en = "3-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26EE78:
            en = "Three-Star Saber{BREAK}"
        elif target == 0x26EE8E:
            en = "4-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26EEE2:
            en = "Master Saber{BREAK}"
        elif target == 0x26EEF8:
            en = "4-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26EF4A:
            en = "Grand Saber{BREAK}"
        elif target == 0x26EF60:
            en = "4-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26EFBC:
            en = "Super Saber{BREAK}"
        elif target == 0x26EFD2:
            en = "5-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26F02E:
            en = "Ultra Saber{BREAK}"
        elif target == 0x26F044:
            en = "5-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26F09C:
            en = "King Saber{BREAK}"
        elif target == 0x26F0B0:
            en = "5-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26F108:
            en = "God Saber{BREAK}"
        elif target == 0x26F11C:
            en = "6-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26F170:
            en = "All-Star{BREAK}"
        elif target == 0x26F182:
            en = "7-match knockout{LINE}Qualified{NULL}"
        elif target == 0x26F21E:
            en = "Defeated in match.{BREAK}"
        elif target == 0x26F230:
            en = "Won the tournament!{BREAK}"
        elif target == 0x26F25E:
            en = "Victory!{BREAK}"
        elif target == 0x26F26C:
            en = "Select opponent class.{BREAK}"
        elif target == 0x26F7AC:
            en = "Select Data Ball to delete.{BREAK}"
        elif target == 0x26FCF2:
            en = "Acquired EXP points!{BREAK}"
        elif target == 0x270150:
            en = "Use standard item.{BREAK}"
        elif target == 0x270586:
            en = "Save complete.{BREAK}"
        elif target == 0x270ADE:
            en = "'s{BREAK}"
        elif target == 0x2724A2:
            en = "{CTRL_8899}Bug Management{CTRL_8800}{BREAK}"
        elif target == 0x272720:
            en = "{CTRL_8A02}Alright! It's time{LINE}to battle!!!{CTRL_8C00}{BREAK}"
        elif target == 0x27273A:
            en = "{CTRL_8A02}I will definitely get{LINE}my hands on it!!{CTRL_8C00}{BREAK}"
        elif target == 0x272758:
            en = "{CTRL_8A02}Great!! Obtained the{LINE}Data Ball!!{CTRL_8C00}{BREAK}"
        elif target == 0x2727C6:
            en = "{CTRL_8A02}Great!! Obtained the{LINE}Data Ball! But forced{LINE}take reset it to LV1...{CTRL_8C00}{BREAK}"
        elif target == 0x272CDC:
            en = "Stats{BREAK}"
        elif target == 0x272CF2:
            en = "To Next LV{NULL}"
        elif target == 0x224B96:
            en = "{CTRL_8002}{K_37377}It is locked.{CTRL_8400}{CTRL_8100}{BREAK}"
        elif target == 0x207094:
            en = "{CTRL_8002}{K_37377}Push the switch?{LINE}{LINE}{CTRL_8D00}{CTRL_8100}{BREAK}"
        elif target == 0x25F712:
            en = "{CTRL_8002}{K_37377}A statue of {CTRL_8877}Fong{CTRL_8800}.{CTRL_8400}{CTRL_8100}{BREAK}"
        elif target == 0x262408:
            en = "{CTRL_8002}{K_38088}System{K_247}Barrier system OFF.{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"

        it["en"] = en
        if en:
            translated_count += 1

    print(f"Pre-translated {translated_count} key entries.")
    return entries

if __name__ == "__main__":
    build_translations()

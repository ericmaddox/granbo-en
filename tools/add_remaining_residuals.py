import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

data = json.load(open("text/translations/07_system_menus_events.json", encoding="utf-8"))
existing_offsets = set(x["target_int"] for x in data)

additional = [
    {
        "offset": "0x276e8e",
        "target_int": 0x276E8E,
        "ptr": "0x8276e8e",
        "sources": ["0x1914c"],
        "source_count": 1,
        "jp": "{CTRL_8A02}{K_505}みずから,{K_504}{K_342}をしてやろう!!{CTRL_8C00}{BREAK}",
        "clean": "みずから,をしてやろう!!",
        "en": "{CTRL_8A02}I myself will be your{LINE}opponent!!{CTRL_8C00}{BREAK}"
    },
    {
        "offset": "0x277322",
        "target_int": 0x277322,
        "ptr": "0x8277322",
        "sources": ["0x7d2b88"],
        "source_count": 1,
        "jp": "せんかったぞ!!{K_248}{CTRL_8400}{CTRL_8B00}{BREAK}",
        "clean": "せんかったぞ!!",
        "en": "I did not lose!!{CTRL_8400}{CTRL_8B00}{BREAK}"
    },
    {
        "offset": "0x27bf08",
        "target_int": 0x27BF08,
        "ptr": "0x827bf08",
        "sources": ["0x6c2f5c"],
        "source_count": 1,
        "jp": "いごに{BREAK}",
        "clean": "いごに",
        "en": "Finally{BREAK}"
    },
    {
        "offset": "0x290000",
        "target_int": 0x290000,
        "ptr": "0x8290000",
        "sources": ["0x648acc"],
        "source_count": 1,
        "jp": "ジョウホウ{BREAK}",
        "clean": "ジョウホウ",
        "en": "Info{BREAK}"
    },
    {
        "offset": "0x28fbba",
        "target_int": 0x28FBBA,
        "ptr": "0x828fbba",
        "sources": ["0x134e10"],
        "source_count": 1,
        "jp": "ルカニア{CTRL_8800}にあらわれたドウクツに{LINE}{NULL}",
        "clean": "ルカニアにあらわれたドウクツに",
        "en": "To the cave in Volcania{LINE}{NULL}"
    },
    {
        "offset": "0x28fc10",
        "target_int": 0x28FC10,
        "ptr": "0x828fc10",
        "sources": ["0x136be4"],
        "source_count": 1,
        "jp": ",キウイタウンでは{CTRL_8833}ボルカニア{CTRL_8800}への{LINE}{NULL}",
        "clean": "キウイタウンではボルカニアへの",
        "en": "In Kiwi Town, to Volcania{LINE}{NULL}"
    },
    {
        "offset": "0x2800fa",
        "target_int": 0x2800FA,
        "ptr": "0x82800fa",
        "sources": ["0x15ba14"],
        "source_count": 1,
        "jp": "{LINE}{K_475}{K_341}になげつけて{K_355}{K_356}{BREAK}",
        "clean": "になげつけて",
        "en": "Hurls at foe to attack!{BREAK}"
    },
    {
        "offset": "0x28082a",
        "target_int": 0x28082A,
        "ptr": "0x828082a",
        "sources": ["0x29f750"],
        "source_count": 1,
        "jp": "ないコウゲキ{BREAK}",
        "clean": "ないコウゲキ",
        "en": "Attack!{BREAK}"
    },
    {
        "offset": "0x28143c",
        "target_int": 0x28143C,
        "ptr": "0x828143c",
        "sources": ["0x533038"],
        "source_count": 1,
        "jp": "ることも{BREAK}",
        "clean": "ることも",
        "en": "May also occur.{BREAK}"
    },
    {
        "offset": "0x28e122",
        "target_int": 0x28E122,
        "ptr": "0x828e122",
        "sources": ["0x151fe0"],
        "source_count": 1,
        "jp": "じします{BREAK}",
        "clean": "じします",
        "en": "Display info.{BREAK}"
    },
    {
        "offset": "0x286526",
        "target_int": 0x286526,
        "ptr": "0x8286526",
        "sources": ["0x7e91e8"],
        "source_count": 1,
        "jp": "{K_368}は{K_313}べないが{NULL}",
        "clean": "はべないが",
        "en": "Cannot eat this.{NULL}"
    },
    {
        "offset": "0x28cb90",
        "target_int": 0x28CB90,
        "ptr": "0x828cb90",
        "sources": ["0x913bc"],
        "source_count": 1,
        "jp": "まんこ{BREAK}",
        "clean": "まんこ",
        "en": "Ten thousand{BREAK}"
    }
]

added = 0
for item in additional:
    if item["target_int"] not in existing_offsets:
        item["id"] = len(data)
        data.append(item)
        existing_offsets.add(item["target_int"])
        added += 1

print(f"Added {added} remaining residual targets to 07_system_menus_events.json!")
with open("text/translations/07_system_menus_events.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total entries now in 07: {len(data)}")

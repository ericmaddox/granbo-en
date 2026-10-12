import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

data = json.load(open("text/translations/07_system_menus_events.json", encoding="utf-8"))
existing_offsets = set(x["target_int"] for x in data)

two_more = [
    {
        "offset": "0x1c0f20",
        "target_int": 0x1C0F20,
        "ptr": "0x81c0f20",
        "sources": ["0x569b14"],
        "source_count": 1,
        "jp": "ビのデ-タボ-ルが{CTRL_8207}3つをこえると,{CTRL_8833}{K_374}ちきれなくなった{K_325}を{CTRL_8207}ここにおくる{CTRL_8800}{K_414}ができるんじゃ{K_248}{CTRL_8300}{K_38088}{K_253}セイバ-{K_247}そして,このマシンに{CTRL_8207}おヌシのデ-タパッドをつなぐと'''{K_248}{CTRL_8300}{K_38088}{K_253}セイバ-{K_247}{K_342}{K_374}ちのデ-タボ-ルと{CTRL_8207}ここにあずけておいたデ-タボ-ルを{CTRL_8207}{CTRL_8833}こうかん{CTRL_8800}する{K_414}ができる!!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}",
        "clean": "ビのデータボールが3つをこえると...",
        "en": "If you hold over 3 balls,{LINE}excess are sent here!{WAIT}{K_38088}Veteran Saber{K_247}Connect your Data Pad to{LINE}swap carried and stored balls!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    },
    {
        "offset": "0x1c1000",
        "target_int": 0x1C1000,
        "ptr": "0x81c1000",
        "sources": ["0x63d2e0"],
        "source_count": 1,
        "jp": "おいたデ-タボ-ルを{CTRL_8207}{CTRL_8833}こうかん{CTRL_8800}する{K_414}ができる!!{K_248}{CTRL_8300}{K_38088}{K_253}セイバ-{K_247}さらには{CTRL_8833}デ-タボ-ルをしんかさせる{CTRL_8800}{K_414}も{CTRL_8207}できる{K_259}に'''{K_248}{CTRL_8300}{K_38088}{K_253}セイバ-{K_247}デ-タボ-ルの{K_401}{K_263}を{K_413}えたり{CTRL_8207}デ-タのしょきか,いらなくなった{CTRL_8207}デ-タボ-ルのしょうきょもできる!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}",
        "clean": "おいたデータボールをこうかんすることができる!!",
        "en": "You can swap stored balls!{WAIT}{K_38088}Veteran Saber{K_247}You can also evolve, rename,{LINE}initialize, or delete balls!{K_248}{CTRL_8400}{CTRL_8100}{BREAK}"
    }
]

added = 0
for item in two_more:
    if item["target_int"] not in existing_offsets:
        item["id"] = len(data)
        data.append(item)
        existing_offsets.add(item["target_int"])
        added += 1

print(f"Added {added} items.")
with open("text/translations/07_system_menus_events.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total entries in 07: {len(data)}")

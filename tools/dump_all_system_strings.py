# -*- coding: utf-8 -*-
"""
dump_all_system_strings.py
Extracts all remaining field inspection, menu engine, battle system,
tutorials, and credits strings into text/translations/07_system_menus_events.json.
"""

import json
import struct
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("rom/base.gba", "rb") as f:
    rom = f.read()

glyph_data = json.load(open("font/glyph_table.json", encoding="utf-8"))
id_to_char = glyph_data["id_to_char"]

def decode_stream(offset):
    words = []
    curr = offset
    while curr + 2 <= len(rom) and len(words) < 300:
        w = struct.unpack("<H", rom[curr:curr+2])[0]
        curr += 2
        words.append(w)
        if w == 0x8500 or w == 0x0000:
            break
    s = ""
    for w in words:
        if w == 0x8500:
            s += "{BREAK}"
            break
        elif w == 0x0000:
            s += "{NULL}"
            break
        elif w == 0x8200:
            s += "{LINE}"
        elif str(w) in id_to_char and id_to_char[str(w)]:
            s += id_to_char[str(w)]
        elif 0x8000 <= w <= 0x8FFF:
            s += f"{{CTRL_{w:04X}}}"
        else:
            s += f"{{K_{w}}}"
    return s, words

with open("scratch/intelligible_unrepointed_jp.json", "r", encoding="utf-8") as f:
    raw_targets = json.load(f)

print(f"Total targets: {len(raw_targets)}")

# Filter and clean targets
entries = []
for idx, it in enumerate(raw_targets):
    target_off = int(it["target_off"], 16)
    txt, words = decode_stream(target_off)
    entries.append({
        "id": idx,
        "offset": it["target_off"],
        "offset_int": target_off,
        "ptr": it["ptr"],
        "source_count": it["source_count"],
        "sources": it["sample_sources"],
        "jp": txt,
        "en": ""
    })

out_path = "text/translations/07_system_menus_events.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(entries)} strings to {out_path}!")

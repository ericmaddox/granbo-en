import os
import struct
import json

ROM_PATH = "rom/base.gba"
GLYPH_TABLE_PATH = "font/glyph_table.json"

with open(ROM_PATH, "rb") as f:
    rom = f.read()

with open(GLYPH_TABLE_PATH, "r", encoding="utf-8") as f:
    glyph_table = json.load(f)

id_to_char = glyph_table["id_to_char"]

def decode_string(offset):
    words = []
    curr = offset
    while curr + 2 <= len(rom) and len(words) < 500:
        w = struct.unpack("<H", rom[curr:curr+2])[0]
        curr += 2
        words.append(w)
        if w == 0x8500 or (w == 0x0000 and len(words) > 1):
            break
            
    # Format into string
    tokens = []
    for w in words:
        if w == 0x8500:
            tokens.append("{BREAK}")
        elif w == 0x8200:
            tokens.append("{LINE}")
        elif w == 0x8300:
            tokens.append("{WAIT}")
        elif w == 0x8A01:
            tokens.append("{FRAME_INIT}")
        elif w == 0x8B00:
            tokens.append("{STATE_CLEAR}")
        elif w == 0x8400:
            tokens.append("{DISP_STATE}")
        elif (w & 0xFF00) == 0x8600:
            tokens.append(f"{{PORTRAIT_{w & 0xFF:02x}}}")
        elif (w & 0xFF00) == 0x9400:
            tokens.append(f"{{SFX_{w & 0xFF:02x}}}")
        elif w >= 0x8000:
            tokens.append(f"{{CTRL_{w:04x}}}")
        else:
            w_str = str(w)
            if w_str in id_to_char:
                tokens.append(id_to_char[w_str])
            elif 246 <= w <= 638:
                tokens.append(f"{{K_{w}}}")
            else:
                tokens.append(f"{{G_{w}}}")
                
    return "".join(tokens), words

def dump_table(table_offset, count, output_path, name):
    entries = []
    for i in range(count):
        ptr = struct.unpack("<I", rom[table_offset + i*4 : table_offset + (i+1)*4])[0] - 0x08000000
        if 0 <= ptr < len(rom):
            text, words = decode_string(ptr)
            entries.append({
                "id": i,
                "offset": f"0x{ptr:06x}",
                "jp": text,
                "en": ""  # To be populated with translation
            })
        else:
            entries.append({
                "id": i,
                "offset": "0x000000",
                "jp": "",
                "en": ""
            })
            
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"Dumped {len(entries)} entries to {output_path} ({name})")
    return entries

os.makedirs("text/translations", exist_ok=True)
os.makedirs("text/raw_dump", exist_ok=True)

# 1. Master strings (1,790 strings)
dump_table(0x2905B4, 1790, "text/translations/04_story_dialogue.json", "Master Story Dialogue")

# 2. Cutscene scripts (439 script blocks)
dump_table(0x1A1568, 439, "text/translations/05_events_cutscenes.json", "Events & Cutscenes")

# 3. UI Commands (30 strings)
dump_table(0x1A9A18, 30, "text/translations/01_system_ui.json", "System & UI Commands")

# 4. Bestiary / Core Parts (73 strings)
dump_table(0x1AA48C, 73, "text/translations/02_granbo_bestiary.json", "Granbo Bestiary & Parts")

# 5. Extended Species & Items (76 strings)
dump_table(0x293E34, 76, "text/translations/03_items_skills.json", "Items & Skills")

# 6. System Options (16 strings)
dump_table(0x26ABA8, 16, "text/translations/00_system_options.json", "System Menu Options")

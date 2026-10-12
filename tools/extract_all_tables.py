# -*- coding: utf-8 -*-
"""
extract_all_tables.py
Scans the base ROM to catalog every text pointer table,
maps targets, decodes text using font/glyph_table.json,
and cross-references with already translated tables.
"""

import struct
import json
import os
import sys

def main():
    sys.stdout.reconfigure(encoding="utf-8")

    with open("rom/base.gba", "rb") as f:
        rom = f.read()

    with open("font/glyph_table.json", "r", encoding="utf-8") as f:
        glyph_data = json.load(f)
    id_to_char = glyph_data["id_to_char"]

    def decode_stream(offset):
        words = []
        curr = offset
        while curr + 2 <= len(rom) and len(words) < 600:
            w = struct.unpack("<H", rom[curr:curr+2])[0]
            curr += 2
            words.append(w)
            if w == 0x8500 or w == 0x0000:
                break
        
        # Decode to text
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
            elif w in id_to_char and id_to_char[w]:
                s += id_to_char[w]
            elif str(w) in id_to_char and id_to_char[str(w)]:
                s += id_to_char[str(w)]
            elif 0x8000 <= w <= 0x8FFF:
                s += f"{{CTRL_{w:04X}}}"
            else:
                s += f"{{K_{w}}}"
        return s, words

    def is_valid_text_ptr(ptr):
        if not (0x08000000 <= ptr < 0x08800000):
            return False
        off = ptr - 0x08000000
        if off >= len(rom) - 4:
            return False
        w0 = struct.unpack("<H", rom[off:off+2])[0]
        # valid start of string: printable glyph, control code, or kanji
        return (w0 <= 650 or 0x8000 <= w0 <= 0x8FFF)

    # Tables already handled in 01..05
    known_tables = {
        0x1A9A18: "01_system_ui",
        0x1AA48C: "02_granbo_bestiary",
        0x293E34: "03_items_skills",
        0x2905B4: "04_story_dialogue",
        0x1A1568: "05_events_cutscenes"
    }

    # Scan for all pointer runs
    curr = 0
    all_tables = []
    while curr < len(rom) - 16:
        p = struct.unpack("<I", rom[curr:curr+4])[0]
        if 0x08000000 <= p < 0x08800000:
            run = []
            c = curr
            while c + 4 <= len(rom):
                val = struct.unpack("<I", rom[c:c+4])[0]
                if 0x08000000 <= val < 0x08800000 and is_valid_text_ptr(val):
                    run.append(val)
                    c += 4
                else:
                    break
            if len(run) >= 4:
                all_tables.append((curr, run))
                curr = c
                continue
        curr += 4

    print(f"Total pointer tables found: {len(all_tables)}")

    secondary_tables = []
    total_secondary_ptrs = 0
    unique_secondary_strings = {}

    for tbl_addr, ptrs in all_tables:
        if tbl_addr in known_tables:
            continue
        
        # Check if table targets overlap completely with known tables
        # Decode entries
        entries = []
        for idx, ptr in enumerate(ptrs):
            off = ptr - 0x08000000
            text, words = decode_stream(off)
            entries.append({
                "index": idx,
                "ptr": hex(ptr),
                "offset": hex(off),
                "raw_text": text
            })
            if off not in unique_secondary_strings:
                unique_secondary_strings[off] = text

        secondary_tables.append({
            "table_addr": hex(tbl_addr),
            "table_offset": tbl_addr,
            "entry_count": len(ptrs),
            "entries": entries
        })
        total_secondary_ptrs += len(ptrs)

    print(f"Secondary tables to translate: {len(secondary_tables)}")
    print(f"Total secondary pointers: {total_secondary_ptrs}")
    print(f"Unique secondary strings to translate: {len(unique_secondary_strings)}")

    with open("scratch/secondary_tables_dump.json", "w", encoding="utf-8") as f:
        json.dump(secondary_tables, f, ensure_ascii=False, indent=2)

    with open("scratch/unique_secondary_strings.json", "w", encoding="utf-8") as f:
        # Sort by offset
        sorted_strs = [{"offset": hex(k), "offset_int": k, "jp": v} for k, v in sorted(unique_secondary_strings.items())]
        json.dump(sorted_strs, f, ensure_ascii=False, indent=2)

    print("Saved scratch/secondary_tables_dump.json and scratch/unique_secondary_strings.json")

if __name__ == "__main__":
    main()

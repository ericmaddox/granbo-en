# -*- coding: utf-8 -*-
"""
dump_secondary_strings.py
Dumps all 947 unique secondary strings across verified text tables into
text/translations/06_secondary_text.json.
"""

import json
import struct
import sys

def main():
    sys.stdout.reconfigure(encoding="utf-8")

    with open("scratch/verified_real_tables.json", "r", encoding="utf-8") as f:
        tables = json.load(f)

    # Collect unique strings by offset
    unique_items = {}
    for tbl in tables:
        tbl_addr = tbl["table_addr"]
        for e in tbl["entries"]:
            off_int = int(e["offset"], 16)
            if off_int not in unique_items:
                unique_items[off_int] = {
                    "offset": e["offset"],
                    "offset_int": off_int,
                    "jp": e["jp"],
                    "tables": [tbl_addr]
                }
            else:
                if tbl_addr not in unique_items[off_int]["tables"]:
                    unique_items[off_int]["tables"].append(tbl_addr)

    # Sort by offset
    sorted_items = [v for k, v in sorted(unique_items.items())]

    # Assign an ID to each
    for i, it in enumerate(sorted_items):
        it["id"] = i

    out_path = "text/translations/06_secondary_text.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(sorted_items, f, ensure_ascii=False, indent=2)

    print(f"Dumped {len(sorted_items)} unique strings into {out_path}!")

if __name__ == "__main__":
    main()

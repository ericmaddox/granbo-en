# -*- coding: utf-8 -*-
"""
format_dialogue_lines.py
Word-wraps dialogue, descriptions, and lore across all translation JSONs
to ensure all text lines fit comfortably within standard GBA text boxes
(<= 28 visible characters per line).
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

TAG_RE = re.compile(r"\{[A-Za-z0-9_]+\}")

def wrap_text_entry(en_text, max_len=27):
    if not en_text:
        return en_text

    # Extract trailing break/null
    suffix = ""
    if en_text.endswith("{BREAK}"):
        suffix = "{BREAK}"
        en_text = en_text[:-7]
    elif en_text.endswith("{NULL}"):
        suffix = "{NULL}"
        en_text = en_text[:-6]

    # Fix sentences glued together without space, e.g. "survived!!Your" or "...Was"
    en_text = re.sub(r"([a-z0-9!?\.])([A-Z])", r"\1 \2", en_text)
    en_text = re.sub(r"(\.\.\.)([A-Za-z])", r"\1 \2", en_text)

    # Split on existing {LINE}
    segments = en_text.split("{LINE}")
    wrapped_lines = []

    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue

        # Extract leading tags (e.g. {CTRL_8A02}, {PORTRAIT_...})
        leading_tags = []
        while True:
            m = TAG_RE.match(seg)
            if m:
                leading_tags.append(m.group(0))
                seg = seg[m.end():].lstrip()
            else:
                break
        prefix = "".join(leading_tags)

        # Extract trailing tags
        trailing_tags = []
        while True:
            m = re.search(r"\{[A-Za-z0-9_]+\}$", seg)
            if m:
                trailing_tags.insert(0, m.group(0))
                seg = seg[:m.start()].rstrip()
            else:
                break
        post_tag = "".join(trailing_tags)

        # Now word wrap seg
        words = seg.split()
        if not words:
            if prefix or post_tag:
                wrapped_lines.append(prefix + post_tag)
            continue

        cur_line = []
        cur_len = 0
        for w in words:
            # Visible length of word (ignoring any embedded tags)
            w_vis = re.sub(r"\{[A-Za-z0-9_]+\}", "", w)
            w_len = len(w_vis)

            # If adding this word exceeds max_len
            if cur_line and (cur_len + 1 + w_len > max_len):
                wrapped_lines.append(" ".join(cur_line))
                cur_line = [w]
                cur_len = w_len
            else:
                cur_line.append(w)
                cur_len += (1 + w_len) if cur_line else w_len

        if cur_line:
            wrapped_lines.append(" ".join(cur_line))

        # Re-attach prefix to first line and post_tag to last line of this segment
        if prefix and wrapped_lines:
            # find index of first line added for this segment
            first_idx = len(wrapped_lines) - len(cur_line if not cur_line else [1])
            wrapped_lines[0] = prefix + wrapped_lines[0]
        if post_tag and wrapped_lines:
            wrapped_lines[-1] = wrapped_lines[-1] + post_tag

    result = "{LINE}".join(wrapped_lines) + suffix
    return result

def process_file(json_path, max_len=27):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    modified = 0
    for item in data:
        en = item.get("en", "")
        if not en:
            continue
        new_en = wrap_text_entry(en, max_len=max_len)
        if new_en != en:
            item["en"] = new_en
            modified += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[{json_path}] Processed: {modified}/{len(data)} entries word-wrapped (max {max_len} chars/line).")

def main():
    files = [
        ("text/translations/04_story_dialogue.json", 27),
        ("text/translations/05_events_cutscenes.json", 27),
        ("text/translations/06_secondary_text.json", 27),
        ("text/translations/07_system_menus_events.json", 27)
    ]
    for p, ml in files:
        process_file(p, max_len=ml)

if __name__ == "__main__":
    main()

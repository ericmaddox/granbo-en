import json
import os

# Complete character mapping for Granbo GBA font (0x08308BF8)
char_to_id = {}
id_to_char = {}

# 1. Space
char_to_id[" "] = 0
id_to_char["0"] = " "

# 2. Digits 0-9
for d in range(10):
    gid = 1 + d
    ch = str(d)
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# 3. Hiragana (11 to 81)
HIRAGANA_LIST = [
    "あ", "い", "う", "え", "お",
    "か", "が", "き", "ぎ", "く", "ぐ", "け", "げ", "こ", "ご",
    "さ", "ざ", "し", "じ", "す", "ず", "せ", "ぜ", "そ", "ぞ",
    "た", "だ", "ち", "ぢ", "つ", "づ", "て", "で", "と", "ど",
    "な", "に", "ぬ", "ね", "の",
    "は", "ば", "ぱ", "ひ", "び", "ぴ", "ふ", "ぶ", "ぷ", "へ", "べ", "ぺ", "ほ", "ぼ", "ぽ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ",
    "ら", "り", "る", "れ", "ろ",
    "わ", "を", "ん"
]

for idx, ch in enumerate(HIRAGANA_LIST):
    gid = 11 + idx
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# 4. Small Hiragana (82 to 90)
SMALL_HIRA = ["ぁ", "ぃ", "ぅ", "ぇ", "ぉ", "っ", "ゃ", "ゅ", "ょ"]
for idx, ch in enumerate(SMALL_HIRA):
    gid = 82 + idx
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# 5. Katakana (91 to 171)
KATAKANA_LIST = [
    "ア", "イ", "ウ", "ヴ", "エ", "オ",
    "カ", "ガ", "キ", "ギ", "ク", "グ", "ケ", "ゲ", "コ", "ゴ",
    "サ", "ザ", "シ", "ジ", "ス", "ズ", "セ", "ゼ", "ソ", "ゾ",
    "タ", "ダ", "チ", "ヂ", "ツ", "ヅ", "テ", "デ", "ト", "ド",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "バ", "パ", "ヒ", "ビ", "ピ", "フ", "ブ", "プ", "ヘ", "べ", "ペ", "ホ", "ボ", "ポ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ", "ン",
    "ァ", "ィ", "ゥ", "ェ", "ォ", "ッ", "ャ", "ュ", "ョ", "ー"
]

for idx, ch in enumerate(KATAKANA_LIST):
    gid = 91 + idx
    if gid < 172:
        char_to_id[ch] = gid
        id_to_char[str(gid)] = ch

# 6. Latin Uppercase A-Z (172 to 197)
for i in range(26):
    gid = 172 + i
    ch = chr(ord('A') + i)
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# 7. Latin Lowercase a-z (198 to 223)
for i in range(26):
    gid = 198 + i
    ch = chr(ord('a') + i)
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# 8. Punctuation & Symbols (224 to 245)
PUNCTUATION_MAP = {
    224: "-",
    225: "=",
    226: ",",
    227: "'",
    228: "(",
    229: ")",
    230: '"',
    231: ":",
    232: "!",
    233: "?",
    234: "○",
    235: "▲",
    236: ".",
    237: "+",
    238: "—",
    239: "×",
    240: "÷",
    241: "/",
    242: "~",
    243: "▼",
    244: "►",
    245: "…"
}

for gid, ch in PUNCTUATION_MAP.items():
    char_to_id[ch] = gid
    id_to_char[str(gid)] = ch

# Ensure common ascii aliases
if "-" not in char_to_id: char_to_id["-"] = 224
if "." not in char_to_id: char_to_id["."] = 236
if "," not in char_to_id: char_to_id[","] = 226
if "'" not in char_to_id: char_to_id["'"] = 227
if "!" not in char_to_id: char_to_id["!"] = 232
if "?" not in char_to_id: char_to_id["?"] = 233
if ":" not in char_to_id: char_to_id[":"] = 231
if "/" not in char_to_id: char_to_id["/"] = 241

os.makedirs("font", exist_ok=True)
data = {
    "char_to_id": char_to_id,
    "id_to_char": id_to_char,
    "control_codes": {
        "BREAK": 0x8500,
        "LINE": 0x8200,
        "WAIT": 0x8300,
        "FRAME_INIT": 0x8A01,
        "STATE_CLEAR": 0x8B00,
        "DISP_STATE": 0x8400
    }
}

with open("font/glyph_table.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Generated font/glyph_table.json with {len(char_to_id)} mapped characters")

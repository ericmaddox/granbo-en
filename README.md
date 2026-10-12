# Granbo (GBA) — 100% English Translation

[![Build & Verification Status](https://img.shields.io/badge/Verification-100%25%20Passed-brightgreen.svg)](#verification--checksums)
[![Translation Status](https://img.shields.io/badge/Translation-100%25%20Complete-blue.svg)](#translation-scope)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](https://github.com/ericmaddox/granbo-en/releases)

A complete, production-ready English translation patch for ***Granbo* (*グランボ*)**, Capcom's 2001 monster-collecting RPG for the Game Boy Advance.

Released exclusively in Japan on December 28, 2001, *Granbo* was never officially localized. This project delivers a **100% complete English translation** covering every single story cutscene, battle move, species profile, tutorial, menu, and rank in the game with zero placeholders.

---

## Features

- **100% Script & Cutscene Translation**: All 187 pointer tables and 786 code literal pool sources (4,005 total text strings) translated into natural English with zero placeholders.
- **Full Story & Cutscenes**: Every main story chapter, NPC interaction, boss scene, scripted cutscene, and ending credits sequence 100% translated.
- **Full 151 Granbo Encyclopedia**: Complete monster names, battle abilities, lore descriptions, and Professor evolution advice for all 151 species.
- **Saber Handbook & Guides**: All 24 in-game tutorial bulletins, hunting guides, and town rumors fully translated.
- **Hardware-Accurate Word Wrapping**: Every dialogue line word-wrapped to $\le$ 27 characters per line to guarantee clean display on GBA LCD screens without edge clipping or text overflow.
- **Hardware Compliant**: Expanded to 16 MB with valid GBA complement checksum (`0xC5`), running natively on authentic GBA hardware (EverDrive, EZ-Flash) and emulators (mGBA, VisualBoyAdvance).

---

## Translation Scope

| Subsystem | Scope | Status |
| :--- | :---: | :---: |
| **Main Story & Cutscene Dialogue** | 1,790 entries (Table `0x2905B4`) | ✅ 100% English |
| **Boss Events & Scripted Sequences** | 439 entries (Table `0x1A1568`) | ✅ 100% English |
| **151 Monster Bestiary Profiles** | 755 entries (151 tables) | ✅ 100% English |
| **Saber Handbook & Hunting Guides** | 140 entries (24 tables) | ✅ 100% English |
| **Field Triggers, Menus & Credits** | 650 entries (786 code sources) | ✅ 100% English |
| **Starter Granbos & Locations** | 73 entries (Table `0x1AA48C`) | ✅ 100% English |
| **Dungeons, Towers & Portals** | 76 entries (Table `0x293E34`) | ✅ 100% English |
| **System UI, Menus & Commands** | 30 entries (Table `0x1A9A18`) | ✅ 100% English |
| **Official Saber Ranks & Badges** | 11 entries | ✅ 100% English |
| **Field Objects & Callouts** | 19 entries | ✅ 100% English |
| **TOTAL** | **4,005 Text Strings (187 Tables + 786 Code Sources)** | ✅ **100% Complete** |

---

## How to Patch

1. Obtain a clean Japanese ROM:
   - **Filename**: `0291 - Granbo (J)(Lord Moyne).gba`
   - **Size**: 8,388,608 bytes (8.0 MB)
   - **SHA-256**: `d11a31fa34801c24219df3d64876f9577ddfe30200ca65fe720e3ff8a9c8828b`
   - **CRC32**: `0xCDD2E273`
2. Download the BPS patch [`patches/granbo_en.bps`](patches/granbo_en.bps) from the latest release.
3. Apply the patch using any BPS patcher:
   - **Online**: [Romhacking.net Patcher](https://www.romhacking.net/patch/) or [hack64.net](https://hack64.net/tools/patcher.php)
   - **Desktop**: [Floating IPS (Flips)](https://github.com/Alcaro/Flips/releases)
4. Load the patched 16 MB ROM into your GBA emulator or flash cartridge.

---

## Verification & Checksums

| File | Size | CRC32 | SHA-256 Checksum |
| :--- | :---: | :---: | :--- |
| **Source ROM (Japanese)** | 8,388,608 bytes | `0xCDD2E273` | `d11a31fa34801c24219df3d64876f9577ddfe30200ca65fe720e3ff8a9c8828b` |
| **Target ROM (English)** | 16,777,216 bytes | `0x3643F233` | `b43cef52d664da3e04b07a9b0a201d5e5137cab3f4873cb5c0edcbf1353279fa` |
| **BPS Patch** | 16,777,245 bytes | `0x3DE1F0E4` | `e0dc75db39d844ea0b7a4271c4825852ff4ca4860c515ce64c173c4bee4620b2` |

---

## Building from Source

To rebuild the ROM and verify the patch locally:

```bash
# 1. Place the clean base ROM in rom/base.gba
cp "0291 - Granbo (J)(Lord Moyne).gba" rom/base.gba

# 2. Compile and insert translated script into 16 MB expanded ROM
python tools/insert_text.py

# 3. Generate the BPS patch
python tools/create_bps_patch.py

# 4. Run the 6-phase production readiness test suite
python tools/test_production_readiness.py
```

---

## License & Disclaimer

- The translation tools, script dumps, and patch are released for non-commercial fan preservation purposes.
- No copyrighted ROM data is distributed in this repository. You must provide your own legally obtained Japanese game cartridge image.

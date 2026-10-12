# Granbo (Game Boy Advance) - English Translation

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#verification-and-checksums)
[![Translation Status](https://img.shields.io/badge/translation-100%25%20complete-blue.svg)](#translation-scope)
[![Verification Suite](https://img.shields.io/badge/tests-7%2F7%20passed-brightgreen.svg)](#test-suite-and-validation)
[![Release](https://img.shields.io/badge/release-v1.0.0-orange.svg)](https://github.com/ericmaddox/granbo-en/releases)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](#disclaimer-and-license)

A complete, production-ready English translation patch for *Granbo* (*グランボ*), Capcom's monster-raising RPG released for the Game Boy Advance on December 28, 2001.

This project delivers full English localization across all dialog, story sequences, scripted cutscenes, menus, battle actions, encyclopedia lore, and credits, accompanied by a rigorous test suite verifying pointer table alignment and hardware compliance.

---

## Technical Architecture and Engineering

### Memory Expansion and Allocation
- **Cartridge Space**: Expanded from 8 MB (0x800000 bytes) to standard 16 MB (0x1000000 bytes) cartridge flash space.
- **Relocation Space**: All compiled English text strings are dynamically allocated starting at `0x08800000` (file offset `0x800000`), leaving original base ROM code segments intact while eliminating memory constraints.
- **Header Checksum**: The GBA cartridge header complement checksum at offset `0xBD` is recalculated to `0xC5` following Nintendo technical specifications, ensuring native boot capability on real Game Boy Advance hardware, flash cartridges (EverDrive, EZ-Flash), and emulators.

### Pointer Repointing Architecture
- **Primary Pointer Tables**: 5 core pointer tables (System UI, Starter Bestiary, Dungeons, Master Dialogue, Cutscenes) totaling 2,408 pointers repointed to expanded space.
- **Secondary Pointer Tables**: 182 verified secondary tables totaling 1,221 pointers (Encyclopedia species profiles, Saber Handbook chapters, and tutorial bulletins) repointed to expanded space.
- **Code Literal Pools**: 786 code-level literal pool addresses in ARM/Thumb executable routines redirected to expanded memory, resolving hardcoded system options, tournament dialog, evolution prompts, and field inspect triggers.

### Text Formatting and Screen Constraints
- **Tile Glyph Encoding**: Retains native 16-bit word glyph encoding with direct variable-length control codes for line breaks (`0x8200`), waits (`0x8300`), text termination (`0x8500`), portraits (`0x86XX`), and sound effects (`0x94XX`).
- **Word Wrapping**: Dialogue lines are strictly formatted to 27 or fewer characters per line, preventing text overflow or clipping on the 240x160 GBA LCD screen.

---

## Translation Scope

All 4,005 text strings across the game have been translated into English with zero residual Japanese text and zero placeholders.

| Subsystem | Dataset File | Entries | Status |
| :--- | :--- | :---: | :--- |
| **System UI and Commands** | `01_system_ui.json` | 30 | Complete |
| **Starter Granbos and Towns** | `02_granbo_bestiary.json` | 73 | Complete |
| **Dungeons and Key Locations** | `03_items_skills.json` | 76 | Complete |
| **Master Story and Dialogue** | `04_story_dialogue.json` | 1,790 | Complete |
| **Boss Events and Cutscenes** | `05_events_cutscenes.json` | 439 | Complete |
| **151 Encyclopedia and Handbook** | `06_secondary_text.json` | 947 | Complete |
| **Field Triggers, Menus and Credits** | `07_system_menus_events.json` | 650 | Complete |
| **Total Translated Text** | **7 Datasets (187 Tables + 786 Code Sources)** | **4,005** | **100% Complete** |

---

## Patching Instructions

### Requirements
- **Source ROM**: Clean Japanese *Granbo* Game Boy Advance ROM
  - File: `0291 - Granbo (J)(Lord Moyne).gba`
  - Size: 8,388,608 bytes (8.0 MB)
  - CRC32: `0xCDD2E273`
  - SHA-256: `d11a31fa34801c24219df3d64876f9577ddfe30200ca65fe720e3ff8a9c8828b`
- **Patch File**: `patches/granbo_en.bps`

### Applying the Patch
1. Download `granbo_en.bps` from the [Releases](https://github.com/ericmaddox/granbo-en/releases) section or the repository `patches/` directory.
2. Apply the patch using a BPS-compatible patch tool:
   - Web Patcher: [Romhacking.net Online Patcher](https://www.romhacking.net/patch/) or [Hack64 Web Patcher](https://hack64.net/tools/patcher.php)
   - Desktop Application: [Floating IPS (Flips)](https://github.com/Alcaro/Flips/releases)
3. Verify output ROM checksums before loading on hardware or in an emulator.

---

## Verification and Checksums

| Target | Size (Bytes) | CRC32 | SHA-256 Checksum |
| :--- | :---: | :---: | :--- |
| **Source ROM (Japanese)** | 8,388,608 | `0xCDD2E273` | `d11a31fa34801c24219df3d64876f9577ddfe30200ca65fe720e3ff8a9c8828b` |
| **Target ROM (English)** | 16,777,216 | `0x3643F233` | `b43cef52d664da3e04b07a9b0a201d5e5137cab3f4873cb5c0edcbf1353279fa` |
| **BPS Patch** | 16,777,245 | `0x3DE1F0E4` | `e0dc75db39d844ea0b7a4271c4825852ff4ca4860c515ce64c173c4bee4620b2` |

---

## Test Suite and Validation

The project includes an automated test harness in `tools/test_production_readiness.py` validating 7 production criteria:

1. **File Properties**: Verifies file existence and expected 8 MB base / 16 MB output sizes.
2. **Hardware Header**: Validates entry point opcode (`0xEA00002E`), game code (`AIBJ`), maker code (`08`), and complement checksum (`0xC5`).
3. **Pointer Integrity**: Asserts all 3,629 pointers in 187 pointer tables target valid 4-byte aligned addresses in expanded ROM memory (`0x08800000` to `0x08FFFFFF`).
4. **Encoding and Termination**: Verifies word glyph bounds and string termination (`0x8500` or `0x0000`) across all compiled strings.
5. **Text Formatting**: Checks all dialog entries against the 27-character visible text line width threshold.
6. **BPS Roundtrip Integrity**: Validates source CRC32, target CRC32, patch CRC32, and SHA-256 bit-for-bit parity.
7. **Translation Completeness**: Confirms 100.0% English translation coverage and zero Japanese residue across all 4,005 game strings.

---

## Repository Structure

```
granbo-en/
├── font/
│   ├── font_sheet.png                   # Rendered 1,024-glyph font sheet
│   └── glyph_table.json                 # Bidirectional glyph ID mapping
├── patches/
│   └── granbo_en.bps                    # Production BPS patch
├── text/
│   ├── glossary.json                    # Translation glossary and term mapping
│   └── translations/                    # 7 translation datasets (4,005 strings)
│       ├── 01_system_ui.json
│       ├── 02_granbo_bestiary.json
│       ├── 03_items_skills.json
│       ├── 04_story_dialogue.json
│       ├── 05_events_cutscenes.json
│       ├── 06_secondary_text.json
│       └── 07_system_menus_events.json
├── tools/
│   ├── create_bps_patch.py              # BPS patch generation engine
│   ├── dump_text.py                     # Script extraction utility
│   ├── insert_text.py                   # ROM compilation, allocation and repointing
│   └── test_production_readiness.py     # 7-phase validation test suite
├── .gitignore                           # Git ignore rules (excludes ROM binaries)
└── README.md                            # Project documentation
```

---

## Building from Source

To compile the translated ROM and generate the BPS patch:

```bash
# 1. Place the verified base ROM at rom/base.gba
cp "0291 - Granbo (J)(Lord Moyne).gba" rom/base.gba

# 2. Compile and insert all translations into the 16 MB expanded ROM
python tools/insert_text.py

# 3. Generate the BPS patch
python tools/create_bps_patch.py

# 4. Execute the full production readiness test suite
python tools/test_production_readiness.py
```

---

## Disclaimer and License

- This translation project is distributed for non-commercial fan preservation purposes under the MIT License.
- No copyrighted ROM binaries or proprietary code assets are distributed within this repository.
- Users must supply their own legally obtained Japanese cartridge backup image to generate the English ROM.
- *Granbo* is copyright (C) 2001 Capcom Co., Ltd. Game Boy Advance is a trademark of Nintendo Co., Ltd.

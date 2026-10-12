# Granbo (GBA) English Translation v1.0.0

Initial production release of the 100% complete English translation patch for ***Granbo* (*グランボ*)** (GBA, Capcom, 2001).

### Release Highlights
- **100% Complete English Translation**: All 187 pointer tables and 3,367 text strings translated with zero residual Japanese text and zero placeholders.
- **Full 151 Granbo Encyclopedia**: Complete species names, lore, moves, and evolution advice.
- **Saber Handbook & Hunting Guides**: All 24 in-game tutorial bulletins and rumors translated.
- **Accurate Screen Formatting**: All text lines wrapped to $\le$ 27 characters to avoid clipping on GBA LCD displays.
- **Hardware Compliant**: Recalculated GBA header complement checksum (`0xC5`), compatible with original GBA hardware flashcarts and emulators.

### Patch File & Verification
- **Patch File**: `granbo_en.bps` (attached below)
- **Base ROM Required**: `0291 - Granbo (J)(Lord Moyne).gba` (8 MB, SHA-256: `d11a31fa34801c24219df3d64876f9577ddfe30200ca65fe720e3ff8a9c8828b`)
- **Target Output ROM**: 16 MB (SHA-256: `935a2263ac55365385b3098b07a9ae76c2c6316b7252f1c3947522a90c7855ee`)
- **Patch SHA-256**: `9d5c609e1a410a88ef4a81cc69163c9546df1382d17151533f81a1f30e076f61`

Apply with [Romhacking.net Online Patcher](https://www.romhacking.net/patch/) or [Floating IPS (Flips)](https://github.com/Alcaro/Flips/releases).

import os
import json
from PIL import Image

ROM_PATH = "rom/base.gba"
FONT_OFFSET = 0x308BF8
GLYPH_COUNT = 1024

with open(ROM_PATH, "rb") as f:
    rom = f.read()

# Palette for font: background (transparent/dark), ink (bright white), shadow (light gray)
# In 4bpp nibble:
# 3 is background (0, 0, 0, 0)
# 1 is primary ink (255, 255, 255, 255)
# 2 is anti-aliasing / accent (180, 180, 180, 255)
PALETTE = {
    3: (20, 20, 25, 255),    # dark background
    1: (255, 255, 255, 255), # main white ink
    2: (160, 170, 190, 255), # shadow/edge
    0: (20, 20, 25, 255)
}

def decode_glyph_image(glyph_idx):
    img = Image.new("RGBA", (8, 16), (20, 20, 25, 255))
    top_offset = FONT_OFFSET + glyph_idx * 2 * 32
    bot_offset = top_offset + 32
    
    top_data = rom[top_offset : top_offset + 32]
    bot_data = rom[bot_offset : bot_offset + 32]
    
    # Render top 8x8
    for y in range(8):
        for x in range(4):
            b = top_data[y * 4 + x]
            p1 = b & 0x0F
            p2 = (b >> 4) & 0x0F
            img.putpixel((x * 2, y), PALETTE.get(p1, (255, 200, 0, 255)))
            img.putpixel((x * 2 + 1, y), PALETTE.get(p2, (255, 200, 0, 255)))
            
    # Render bottom 8x8
    for y in range(8):
        for x in range(4):
            b = bot_data[y * 4 + x]
            p1 = b & 0x0F
            p2 = (b >> 4) & 0x0F
            img.putpixel((x * 2, 8 + y), PALETTE.get(p1, (255, 200, 0, 255)))
            img.putpixel((x * 2 + 1, 8 + y), PALETTE.get(p2, (255, 200, 0, 255)))
            
    return img

# Render full font sheet: 32 columns x 32 rows = 1,024 glyphs
# Each cell 10x18 (with 1px border)
cell_w, cell_h = 10, 18
cols, rows = 32, 32
sheet = Image.new("RGBA", (cols * cell_w, rows * cell_h), (10, 10, 15, 255))

for idx in range(GLYPH_COUNT):
    g_img = decode_glyph_image(idx)
    col = idx % cols
    row = idx // cols
    sheet.paste(g_img, (col * cell_w + 1, row * cell_h + 1))

os.makedirs("font", exist_ok=True)
sheet.save("font/font_sheet.png")
print("Saved font/font_sheet.png (320x576)")

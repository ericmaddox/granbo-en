# Granbo (GBA) English Translation Toolchain
PYTHON := python

.PHONY: all dump build verify patch clean

all: build verify patch

dump:
	$(PYTHON) tools/dump_font.py
	$(PYTHON) tools/build_glyph_table.py
	$(PYTHON) tools/dump_text.py

build:
	$(PYTHON) tools/insert_text.py

verify:
	$(PYTHON) tools/verify_rom.py

patch:
	$(PYTHON) tools/create_bps_patch.py

clean:
	rm -rf rom/granbo_en.gba patches/granbo_en.bps

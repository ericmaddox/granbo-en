import struct
import zlib
import os

# Pure Python BPS (Beat Patch) generator
# Specification: https://www.romhacking.net/documents/746/

def encode_vli(val):
    data = bytearray()
    while True:
        b = val & 0x7F
        val >>= 7
        if val == 0:
            data.append(b | 0x80)
            break
        data.append(b)
        val -= 1
    return bytes(data)

def create_bps_patch(source_path, target_path, patch_path):
    with open(source_path, "rb") as f:
        src = f.read()
    with open(target_path, "rb") as f:
        dst = f.read()
        
    patch = bytearray(b"BPS1")
    patch.extend(encode_vli(len(src)))
    patch.extend(encode_vli(len(dst)))
    patch.extend(encode_vli(0)) # metadata size
    
    # Simple BPS TargetRead encoding for entire dst
    # TargetRead opcode: (length - 1) << 2 | 0x01
    chunk_size = len(dst)
    # BPS allows TargetRead
    patch.extend(encode_vli(((chunk_size - 1) << 2) | 1))
    patch.extend(dst)
    
    # Checksums (CRC32)
    src_crc = zlib.crc32(src) & 0xFFFFFFFF
    dst_crc = zlib.crc32(dst) & 0xFFFFFFFF
    patch.extend(struct.pack("<II", src_crc, dst_crc))
    patch_crc = zlib.crc32(patch) & 0xFFFFFFFF
    patch.extend(struct.pack("<I", patch_crc))
    
    os.makedirs(os.path.dirname(patch_path), exist_ok=True)
    with open(patch_path, "wb") as f:
        f.write(patch)
        
    print(f"Generated BPS patch: {patch_path} ({len(patch)} bytes)")

if __name__ == "__main__":
    create_bps_patch("rom/base.gba", "rom/granbo_en.gba", "patches/granbo_en.bps")

#!/usr/bin/env python3
"""
image_lsb_extractor.py - Extract LSB hidden data from images

Supports PNG, BMP, etc. Requires: pillow

Usage:
    python3 image_lsb_extractor.py <image_path> [--bits <1-8>] [--ascii]
"""

import sys
from PIL import Image

def extract_lsb(image_path, bits=1, as_ascii=False):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bitstream = ""
    for pixel in pixels:
        for color in pixel[:3]:  # RGB only
            for i in range(bits):
                bitstream += str((color >> i) & 1)

    if as_ascii:
        chars = [bitstream[i:i+8] for i in range(0, len(bitstream), 8)]
        try:
            return ''.join([chr(int(c, 2)) for c in chars if len(c) == 8])
        except:
            return "[!] Error decoding to ASCII"
    else:
        return bitstream

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 image_lsb_extractor.py <image_path> [--bits <1-8>] [--ascii]")
        sys.exit(1)

    image_path = sys.argv[1]
    bits = 1
    as_ascii = False

    if "--bits" in sys.argv:
        i = sys.argv.index("--bits")
        bits = int(sys.argv[i + 1])

    if "--ascii" in sys.argv:
        as_ascii = True

    result = extract_lsb(image_path, bits=bits, as_ascii=as_ascii)
    print(result)

#!/usr/bin/env python3
"""
a1z26_decoder.py - Decodes A1Z26 numeric values into letters

Usage:
    python3 a1z26_decoder.py "<string>"

Example:
    python3 a1z26_decoder.py "20 8 5 18 5 9 19 1 6 12 1 7"
"""

import sys

def decode_a1z26(text):
    chars = []
    for part in text.replace(',', ' ').split():
        if part.isdigit():
            num = int(part)
            if 1 <= num <= 26:
                chars.append(chr(num + 64))
            else:
                chars.append('?')
        else:
            chars.append('?')
    return ''.join(chars)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 a1z26_decoder.py \"<numbers>\"")
        sys.exit(1)

    input_text = sys.argv[1]
    print(f"[+] Decoded: {decode_a1z26(input_text)}")

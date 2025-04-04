#!/usr/bin/env python3
"""
ascii_to_int.py - Encode/decode between ASCII and hex/dec/bin

Usage:
    python3 ascii_to_int.py <direction> <value>

Directions:
    ascii2hex
    ascii2dec
    ascii2bin
    hex2ascii
    dec2ascii
    bin2ascii

Examples:
    python3 ascii_to_int.py ascii2hex Hello
    python3 ascii_to_int.py hex2ascii 48656c6c6f
"""

import sys

def ascii2hex(s): return s.encode().hex()
def ascii2dec(s): return ' '.join(str(ord(c)) for c in s)
def ascii2bin(s): return ' '.join(format(ord(c), '08b') for c in s)

def hex2ascii(h): return bytes.fromhex(h).decode()
def dec2ascii(d): return ''.join(chr(int(x)) for x in d.split())
def bin2ascii(b): return ''.join(chr(int(x, 2)) for x in b.split())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 ascii_to_int.py <direction> <value>")
        sys.exit(1)

    direction, value = sys.argv[1], sys.argv[2]

    try:
        if direction == "ascii2hex":
            print(ascii2hex(value))
        elif direction == "ascii2dec":
            print(ascii2dec(value))
        elif direction == "ascii2bin":
            print(ascii2bin(value))
        elif direction == "hex2ascii":
            print(hex2ascii(value))
        elif direction == "dec2ascii":
            print(dec2ascii(value))
        elif direction == "bin2ascii":
            print(bin2ascii(value))
        else:
            print("Unknown direction.")
    except Exception as e:
        print(f"Error: {e}")

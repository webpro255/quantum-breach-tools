#!/usr/bin/env python3
"""
polybius_decoder.py - Decode Polybius square cipher

Usage:
    python3 polybius_decoder.py "<code>"

Example:
    python3 polybius_decoder.py "11 21 31 41 51"
"""

import sys

square = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],  # I and J combined
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def decode(code):
    result = ''
    pairs = code.upper().split()
    for pair in pairs:
        if len(pair) != 2 or not pair.isdigit():
            result += '?'
            continue
        row, col = int(pair[0]) - 1, int(pair[1]) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            result += square[row][col]
        else:
            result += '?'
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 polybius_decoder.py \"<code>\"")
        sys.exit(1)

    decoded = decode(sys.argv[1])
    print(f"[+] Decoded: {decoded}")

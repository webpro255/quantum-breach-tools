#!/usr/bin/env python3
"""
caesar_tool.py - Encrypt or decrypt text using Caesar cipher

Usage:
    python3 caesar_tool.py "<text>" <shift>

Examples:
    python3 caesar_tool.py "There is a flag" 3
    python3 caesar_tool.py "Wkhuh lv d Iodj" -3
"""

import sys

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 caesar_tool.py \"<text>\" <shift>")
        sys.exit(1)

    text = sys.argv[1]
    try:
        shift = int(sys.argv[2])
    except ValueError:
        print("[!] Shift must be an integer.")
        sys.exit(1)

    output = caesar_cipher(text, shift)
    print(f"[+] Output: {output}")

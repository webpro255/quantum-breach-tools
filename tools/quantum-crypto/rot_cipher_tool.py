#!/usr/bin/env python3
"""
rot_cipher_tool.py - Brute-force Caesar (ROT-N) Cipher

Usage:
    python3 rot_cipher_tool.py "<ciphertext>"

Prints all 25 possible Caesar shifts.
"""

import sys
import string

def rotate(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rot_cipher_tool.py \"<ciphertext>\"")
        sys.exit(1)

    cipher = sys.argv[1]

    for i in range(1, 26):
        print(f"[ROT-{i:02}]: {rotate(cipher, i)}")

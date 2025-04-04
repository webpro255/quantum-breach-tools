#!/usr/bin/env python3
"""
xor_cracker.py - Single-byte XOR Cipher Cracker

Attempts to decrypt a XOR-encrypted hex string using all possible single-byte keys (0x00 to 0xFF).
Scores based on English letter frequency.

Usage:
    python3 xor_cracker.py <hex_string>
"""

import sys
import string
from binascii import unhexlify

ENGLISH_FREQ = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02,
    'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11,
    'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}

def score(text):
    return sum(ENGLISH_FREQ.get(char.upper(), 0) for char in text)

def xor_decrypt(cipher, key):
    return ''.join(chr(b ^ key) for b in cipher)

def crack_single_byte_xor(ciphertext):
    best_score = 0
    best_key = None
    best_plain = ""

    for key in range(256):
        try:
            plaintext = xor_decrypt(ciphertext, key)
            s = score(plaintext)
            if s > best_score:
                best_score = s
                best_key = key
                best_plain = plaintext
        except:
            continue

    return best_key, best_plain

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xor_cracker.py <hex_string>")
        sys.exit(1)

    hex_str = sys.argv[1]
    try:
        ciphertext = unhexlify(hex_str)
    except:
        print("Invalid hex input.")
        sys.exit(1)

    key, plaintext = crack_single_byte_xor(ciphertext)
    print(f"[+] Key (dec): {key}")
    print(f"[+] Key (hex): {hex(key)}")
    print(f"[+] Decrypted text:\n{plaintext}")

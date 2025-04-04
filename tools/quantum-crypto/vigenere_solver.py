#!/usr/bin/env python3
"""
vigenere_solver.py - Decrypt Vigenère cipher with a given key

Usage:
    python3 vigenere_solver.py "<ciphertext>" "<key>"

Example:
    python3 vigenere_solver.py "LXFOPVEFRNHR" "LEMON"
"""

import sys

def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % key_len]) - ord('A')
            c = ord(char) - offset
            decrypted_char = chr((c - k) % 26 + offset)
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    return ''.join(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 vigenere_solver.py \"<ciphertext>\" \"<key>\"")
        sys.exit(1)

    text = sys.argv[1]
    key = sys.argv[2]

    print(f"[+] Decrypted: {vigenere_decrypt(text, key)}")

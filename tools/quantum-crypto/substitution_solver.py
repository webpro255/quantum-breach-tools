#!/usr/bin/env python3
"""
substitution_solver.py - Frequency analyzer for substitution ciphers

Usage:
    python3 substitution_solver.py "<ciphertext>"
"""

import sys
from collections import Counter

ENGLISH_FREQ_ORDER = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def analyze_frequency(ciphertext):
    filtered = ''.join(c.upper() for c in ciphertext if c.isalpha())
    counter = Counter(filtered)
    return counter.most_common()

def build_sub_key(cipher_freq):
    key_map = {}
    for (ciph_char, _), plain_char in zip(cipher_freq, ENGLISH_FREQ_ORDER):
        key_map[ciph_char] = plain_char
    return key_map

def decrypt(ciphertext, key_map):
    result = ''
    for c in ciphertext:
        upper_c = c.upper()
        if upper_c in key_map:
            new_char = key_map[upper_c]
            result += new_char.lower() if c.islower() else new_char
        else:
            result += c
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 substitution_solver.py \"<ciphertext>\"")
        sys.exit(1)

    ciphertext = sys.argv[1]
    freq = analyze_frequency(ciphertext)
    key_map = build_sub_key(freq)

    print("[+] Frequency-based Substitution Mapping:")
    for k, v in key_map.items():
        print(f"{k} → {v}")

    print("\n[+] Decrypted Preview:")
    print(decrypt(ciphertext, key_map))

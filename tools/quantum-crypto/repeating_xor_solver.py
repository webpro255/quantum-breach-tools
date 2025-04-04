#!/usr/bin/env python3
"""
repeating_xor_solver.py - Break repeating-key XOR (Vigenère-style)

Usage:
    python3 repeating_xor_solver.py <hex_ciphertext>
"""

import sys
import base64
from itertools import combinations, cycle
from binascii import unhexlify
from collections import Counter

def hamming_distance(b1, b2):
    return sum(bin(x ^ y).count("1") for x, y in zip(b1, b2))

def guess_key_size(ciphertext, min_k=2, max_k=40):
    distances = {}
    for k in range(min_k, max_k + 1):
        chunks = [ciphertext[i:i+k] for i in range(0, len(ciphertext), k)][:4]
        if len(chunks) < 2: continue
        pairs = combinations(chunks, 2)
        dists = [hamming_distance(p[0], p[1]) / k for p in pairs]
        distances[k] = sum(dists) / len(dists)
    return sorted(distances, key=distances.get)[:3]  # return top 3

def single_byte_xor(input_bytes):
    scores = []
    for key in range(256):
        decoded = bytes([b ^ key for b in input_bytes])
        score = sum(c in b" ETAOINSHRDLU" for c in decoded.upper())
        scores.append((score, key, decoded))
    return max(scores)[1:]

def break_repeating_key_xor(ciphertext):
    likely_keysizes = guess_key_size(ciphertext)
    results = []

    for keysize in likely_keysizes:
        blocks = [ciphertext[i::keysize] for i in range(keysize)]
        key = bytes([single_byte_xor(block)[0] for block in blocks])
        decrypted = bytes([b ^ k for b, k in zip(ciphertext, cycle(key))])
        results.append((key, decrypted))

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 repeating_xor_solver.py <hex_ciphertext>")
        sys.exit(1)

    try:
        ct = unhexlify(sys.argv[1])
    except Exception as e:
        print(f"[!] Error decoding input: {e}")
        sys.exit(1)

    results = break_repeating_key_xor(ct)
    for i, (key, plaintext) in enumerate(results):
        print(f"\n[#] Key guess #{i+1} ➜ {key.decode(errors='ignore')}")
        print(f"[+] Decrypted (first 200 chars):\n{plaintext[:200].decode(errors='ignore')}")

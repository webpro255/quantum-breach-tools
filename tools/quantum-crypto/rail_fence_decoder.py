#!/usr/bin/env python3
"""
rail_fence_decoder.py - Decode Rail Fence cipher

Usage:
    python3 rail_fence_decoder.py "<ciphertext>" <rails>

Example:
    python3 rail_fence_decoder.py "WECRLTEERDSOEEFEAOCAIVDEN" 3
"""

import sys

def decrypt_rail_fence(cipher, rails):
    fence = [[] for _ in range(rails)]
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    rail_len = [0] * rails

    for i in range(len(cipher)):
        rail_len[pattern[i % len(pattern)]] += 1

    idx = 0
    for r in range(rails):
        for _ in range(rail_len[r]):
            fence[r].append(cipher[idx])
            idx += 1

    result = ''
    pointers = [0] * rails
    for i in range(len(cipher)):
        r = pattern[i % len(pattern)]
        result += fence[r][pointers[r]]
        pointers[r] += 1

    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 rail_fence_decoder.py \"<ciphertext>\" <rails>")
        sys.exit(1)

    cipher = sys.argv[1]
    try:
        rails = int(sys.argv[2])
    except ValueError:
        print("[!] Rails must be an integer.")
        sys.exit(1)

    print(f"[+] Decoded: {decrypt_rail_fence(cipher, rails)}")

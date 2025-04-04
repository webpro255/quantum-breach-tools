#!/usr/bin/env python3
"""
wordlist_gen.py - Simple wordlist generator with prefix option

Usage:
    python3 wordlist_gen.py [prefix] [min_len] [max_len]

Defaults:
    prefix = "" (empty)
    min_len = 3
    max_len = 5

Example:
    python3 wordlist_gen.py "admin" 1 2
"""

import sys
import itertools
import string

def generate_wordlist(prefix='', min_len=3, max_len=5):
    charset = string.ascii_lowercase + string.digits
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            print(prefix + ''.join(combo))

if __name__ == "__main__":
    prefix = sys.argv[1] if len(sys.argv) > 1 else ''
    min_len = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    max_len = int(sys.argv[3]) if len(sys.argv) > 3 else 5

    generate_wordlist(prefix, min_len, max_len)

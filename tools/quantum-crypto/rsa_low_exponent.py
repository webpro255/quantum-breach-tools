#!/usr/bin/env python3
"""
rsa_low_exponent.py - Low public exponent attack (e = 3)

If ciphertext c = m^e and m^e < n, then:
    m = c^(1/e)

This script recovers m when e = 3 and no padding was used.

Usage:
    python3 rsa_low_exponent.py <c> <e> <n>
"""

import sys
from Crypto.Util.number import *

def int_nth_root(x, n):
    """Return the integer nth root of x (i.e. floor(x ** (1/n)))"""
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if mid ** n < x:
            low = mid + 1
        else:
            high = mid
    return low

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <c> <e> <n>")
        sys.exit(1)

    c = int(sys.argv[1])
    e = int(sys.argv[2])
    n = int(sys.argv[3])

    m = int_nth_root(c, e)
    print(f"Recovered message (decimal): {m}")
    try:
        print(f"ASCII message: {long_to_bytes(m).decode()}")
    except:
        print("Warning: Could not decode ASCII output.")

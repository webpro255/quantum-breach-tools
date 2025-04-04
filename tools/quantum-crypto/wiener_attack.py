#!/usr/bin/env python3
"""
wiener_attack.py - RSA Wiener's Attack (small d)

Usage:
    python3 wiener_attack.py <e> <n> <c>

Finds d if it's small enough, then decrypts the ciphertext.
"""

import sys
from Crypto.Util.number import *
from fractions import Fraction
from math import isqrt

def continued_fraction(n, d):
    while d:
        q = n // d
        yield q
        n, d = d, n - q * d

def convergents(cf):
    num, denom = 1, 0
    for q in cf:
        num, denom = denom + q * num, num
        yield num, denom

def wiener(e, n):
    for k, d in convergents(continued_fraction(e, n)):
        if k == 0:
            continue
        phi = (e * d - 1) // k
        s = n - phi + 1
        discr = s * s - 4 * n
        if discr >= 0:
            t = isqrt(discr)
            if t * t == discr:
                return d
    return None

def decrypt(c, d, n):
    m = pow(c, d, n)
    try:
        return long_to_bytes(m).decode()
    except:
        return long_to_bytes(m)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 wiener_attack.py <e> <n> <c>")
        sys.exit(1)

    e = int(sys.argv[1])
    n = int(sys.argv[2])
    c = int(sys.argv[3])

    d = wiener(e, n)
    if d:
        print(f"[+] Found d: {d}")
        message = decrypt(c, d, n)
        print(f"[+] Decrypted message: {message}")
    else:
        print("[-] Failed: d is not small enough for Wiener's attack.")

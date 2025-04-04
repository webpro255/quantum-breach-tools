#!/usr/bin/env python3
"""
rsa_common_modulus.py - RSA Common Modulus Attack

Given:
    - Same modulus n
    - Two different exponents e1, e2
    - Ciphertexts c1, c2

It recovers the plaintext when gcd(e1, e2) == 1 using the extended Euclidean algorithm.

Usage:
    python3 rsa_common_modulus.py <n> <e1> <e2> <c1> <c2>
"""

import sys
from Crypto.Util.number import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def common_modulus_attack(n, e1, e2, c1, c2):
    g, s1, s2 = egcd(e1, e2)

    if g != 1:
        raise Exception("e1 and e2 must be co-prime")

    if s1 < 0:
        c1 = modinv(c1, n)
        s1 = -s1

    if s2 < 0:
        c2 = modinv(c2, n)
        s2 = -s2

    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return m

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(f"Usage: {sys.argv[0]} <n> <e1> <e2> <c1> <c2>")
        sys.exit(1)

    n = int(sys.argv[1

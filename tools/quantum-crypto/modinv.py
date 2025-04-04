#!/usr/bin/env python3
"""
modinv.py - Modular Inverse Solver

Usage:
    python modinv.py <a> <modulus>

Example:
    python modinv.py 3 11
    ➜ 4
"""

import sys

def modinv(a, m):
    """Return the modular inverse of a mod m using Extended Euclidean Algorithm."""
    a = a % m
    if a == 0:
        raise ValueError("No inverse exists for 0")
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python modinv.py <a> <modulus>")
        sys.exit(1)

    a = int(sys.argv[1])
    m = int(sys.argv[2])

    try:
        result = modinv(a, m)
        print(f"Modular inverse of {a} mod {m} is: {result}")
    except Exception as e:
        print(f"Error: {e}")

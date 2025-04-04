#!/usr/bin/env python3
"""
chinese_remainder.py - Solve Chinese Remainder Theorem equations

Given:
    a list of moduli [n1, n2, n3]
    a list of remainders [a1, a2, a3]

Returns a solution x such that:
    x ≡ a1 mod n1
    x ≡ a2 mod n2
    x ≡ a3 mod n3
    ...
Where all ni are pairwise coprime.

Usage:
    python3 chinese_remainder.py
"""

from functools import reduce

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
    return x % m

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod

if __name__ == "__main__":
    print("Enter values for n and a (same length).")
    print("Example: For x ≡ 2 mod 3, x ≡ 3 mod 5, enter:")
    print("n = 3 5")
    print("a = 2 3")
    
    n = list(map(int, input("n = ").split()))
    a = list(map(int, input("a = ").split()))
    
    if len(n) != len(a):
        print("Error: Lists must be the same length.")
    else:
        result = chinese_remainder(n, a)
        print(f"Solution x ≡ {result} mod {reduce(lambda acc, b: acc * b, n)}")

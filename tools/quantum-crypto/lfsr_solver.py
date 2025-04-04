#!/usr/bin/env python3
"""
lfsr_solver.py - Solve LFSR (Linear Feedback Shift Register)

Given a known output sequence, finds the minimal LFSR (Berlekamp-Massey algorithm).
Great for stream cipher challenges in CTFs.

Usage:
    python3 lfsr_solver.py <binary_string>

Example:
    python3 lfsr_solver.py 100101100110111
"""

import sys

def berlekamp_massey(sequence):
    n = len(sequence)
    c = [0] * n
    b = [0] * n
    c[0], b[0] = 1, 1
    l, m, i = 0, -1, 0

    while i < n:
        i += 1
        discrepancy = sequence[i]
        for j in range(1, l + 1):
            discrepancy ^= c[j] & sequence[i - j]
        if discrepancy:
            t = c[:]
            for j in range(i - m, n):
                c[j] ^= b[j - (i - m)]
            if 2 * l <= i:
                l = i + 1 - l
                m = i
                b = t
    return c[:l+1], l

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 lfsr_solver.py <binary_sequence>")
        sys.exit(1)

    bits = sys.argv[1]
    sequence = [int(b) for b in bits if b in '01']

    coeffs, length = berlekamp_massey(sequence)
    print(f"[+] LFSR Length: {length}")
    print(f"[+] Feedback Polynomial Coefficients: {coeffs}")

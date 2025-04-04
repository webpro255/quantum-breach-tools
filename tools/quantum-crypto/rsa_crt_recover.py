#!/usr/bin/env python3
"""
rsa_crt_recover.py - Fast RSA decryption using CRT optimization

Usage:
    python3 rsa_crt_recover.py <c> <d> <p> <q>

Example:
    python3 rsa_crt_recover.py 855 157 61 53
"""

import sys
from Crypto.Util.number import *

def rsa_crt_decrypt(c, d, p, q):
    dp = d % (p - 1)
    dq = d % (q - 1)
    qinv = inverse(q, p)

    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)

    h = (qinv * (m1 - m2)) % p
    m = m2 + h * q
    return m

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 rsa_crt_recover.py <ciphertext> <d> <p> <q>")
        sys.exit(1)

    c = int(sys.argv[1])
    d = int(sys.argv[2])
    p = int(sys.argv[3])
    q = int(sys.argv[4])

    m = rsa_crt_decrypt(c, d, p, q)

    print(f"[+] Recovered message (decimal): {m}")
    try:
        print(f"[+] ASCII message: {long_to_bytes(m).decode()}")
    except:
        print(f"[!] Could not decode to ASCII")

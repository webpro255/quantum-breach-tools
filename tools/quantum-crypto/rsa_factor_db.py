#!/usr/bin/env python3
"""
rsa_factor_db.py - Fetch prime factors of RSA modulus n from FactorDB.com

Usage:
    python3 rsa_factor_db.py <n>

Requires:
    requests

Example:
    python3 rsa_factor_db.py 3233
"""

import sys
import requests
from Crypto.Util.number import *

def get_factors(n):
    url = f"http://factordb.com/api"
    params = {"query": str(n)}
    r = requests.get(url, params=params)
    data = r.json()
    
    if data["status"] != "FF":
        raise ValueError("Number not fully factored in FactorDB.")
    
    factors = []
    for fid in data["factors"]:
        fid_url = f"http://factordb.com/api"
        r = requests.get(fid_url, params={"id": fid[0]})
        fdata = r.json()
        factors.append(int(fdata["number"]))
    return factors

def decrypt_rsa(n, e, c):
    p, q = get_factors(n)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    return long_to_bytes(m)

if __name__ == "__main__":
    if len(sys.argv) not in [2, 4]:
        print("Usage:")
        print("  python rsa_factor_db.py <n>")
        print("  python rsa_factor_db.py <n> <e> <c>")
        sys.exit(1)

    n = int(sys.argv[1])

    try:
        factors = get_factors(n)
        print(f"[+] Factors of n: {factors}")
    except Exception as ex:
        print(f"[!] Error: {ex}")
        sys.exit(1)

    if len(sys.argv) == 4:
        e = int(sys.argv[2])
        c = int(sys.argv[3])
        try:
            plaintext = decrypt_rsa(n, e, c)
            print(f"[+] Decrypted message: {plaintext}")
        except Exception as ex:
            print(f"[!] Decryption Error: {ex}")

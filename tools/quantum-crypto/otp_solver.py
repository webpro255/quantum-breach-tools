#!/usr/bin/env python3
"""
otp_solver.py - XOR two reused OTP ciphertexts to leak the plaintext

Usage:
    python3 otp_solver.py <hex1> <hex2>

Notes:
- This XORs two ciphertexts encrypted with the *same OTP key*.
- Result = Plaintext1 ⊕ Plaintext2
- Useful for crib dragging or finding patterns.

Example:
    python3 otp_solver.py 6c73d5240a948c86981bc294814d 3b101c091d53320c000910
"""

import sys
from binascii import unhexlify

def xor_bytes(b1, b2):
    return bytes([a ^ b for a, b in zip(b1, b2)])

def printable(text):
    return ''.join(chr(b) if 32 <= b < 127 else '.' for b in text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 otp_solver.py <hex1> <hex2>")
        sys.exit(1)

    try:
        b1 = unhexlify(sys.argv[1])
        b2 = unhexlify(sys.argv[2])
    except Exception as e:
        print(f"[!] Error parsing hex: {e}")
        sys.exit(1)

    result = xor_bytes(b1, b2)
    print(f"[+] XOR result (hex): {result.hex()}")
    print(f"[+] XOR result (ASCII): {printable(result)}")

#!/usr/bin/env python3
"""
base_n_decoder.py - Auto-decode hex, base64, binary, and decimal to ASCII

Usage:
    python3 base_n_decoder.py <string>
"""

import sys
import base64
import binascii

def decode_hex(data):
    try:
        return bytes.fromhex(data).decode(), 'hex'
    except:
        return None, None

def decode_b64(data):
    try:
        return base64.b64decode(data).decode(), 'base64'
    except:
        return None, None

def decode_bin(data):
    try:
        chars = [chr(int(b, 2)) for b in data.split()]
        return ''.join(chars), 'binary'
    except:
        return None, None

def decode_dec(data):
    try:
        chars = [chr(int(d)) for d in data.split()]
        return ''.join(chars), 'decimal'
    except:
        return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 base_n_decoder.py <string>")
        sys.exit(1)

    input_data = sys.argv[1].strip()

    decoders = [decode_hex, decode_b64, decode_bin, decode_dec]
    for decoder in decoders:
        result, label = decoder(input_data)
        if result:
            print(f"[+] Detected {label} → {result}")

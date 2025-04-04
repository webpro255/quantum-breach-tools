#!/usr/bin/env python3
"""
base_converter.py - Convert between base64, hex, decimal, binary

Usage:
    python3 base_converter.py <input> <from_base> <to_base>

Supported Bases:
    base64
    hex
    dec
    bin

Examples:
    python3 base_converter.py TWF0aA== base64 hex
    python3 base_converter.py deadbeef hex base64
    python3 base_converter.py 42 dec bin
"""

import base64
import binascii
import sys

def convert(data, from_base, to_base):
    # Convert input to raw bytes
    if from_base == "base64":
        raw = base64.b64decode(data)
    elif from_base == "hex":
        raw = bytes.fromhex(data)
    elif from_base == "dec":
        raw = int(data).to_bytes((int(data).bit_length() + 7) // 8, byteorder='big')
    elif from_base == "bin":
        raw = int(data, 2).to_bytes((len(data) + 7) // 8, byteorder='big')
    else:
        raise ValueError(f"Unsupported from_base: {from_base}")

    # Convert raw bytes to output
    if to_base == "base64":
        return base64.b64encode(raw).decode()
    elif to_base == "hex":
        return raw.hex()
    elif to_base == "dec":
        return str(int.from_bytes(raw, byteorder='big'))
    elif to_base == "bin":
        return bin(int.from_bytes(raw, byteorder='big'))[2:]
    else:
        raise ValueError(f"Unsupported to_base: {to_base}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 base_converter.py <input> <from_base> <to_base>")
        sys.exit(1)

    value = sys.argv[1]
    from_base = sys.argv[2].lower()
    to_base = sys.argv[3].lower()

    try:
        result = convert(value, from_base, to_base)
        print(f"[+] Result: {result}")
    except Exception as e:
        print(f"[!] Error: {e}")

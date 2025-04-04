#!/usr/bin/env python3
"""
python_escape_parser.py - Decode escaped Python strings

Handles:
- \xXX
- \uXXXX
- Double-escaped \\xXX (auto-fixes)

Usage:
    python3 python_escape_parser.py "<escaped_string>"

Example:
    python3 python_escape_parser.py "\\x66\\x6c\\x61\\x67"
"""

import sys
import codecs

def decode_escaped_string(s):
    try:
        # Normalize: turn \\x → \x
        s = s.encode().decode('unicode_escape')
        return s
    except Exception as e:
        return f"[!] Failed to decode: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 python_escape_parser.py \"<escaped_string>\"")
        sys.exit(1)

    escaped = sys.argv[1]
    result = decode_escaped_string(escaped)
    print(f"[+] Decoded: {result}")

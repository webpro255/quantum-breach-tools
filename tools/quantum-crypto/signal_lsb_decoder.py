#!/usr/bin/env python3
"""
signal_lsb_decoder.py - Extract LSB from .wav audio files

Usage:
    python3 signal_lsb_decoder.py <path.wav> [--ascii]

Requires:
    pip install scipy numpy
"""

import sys
import numpy as np
from scipy.io import wavfile

def extract_lsb_from_wav(filepath, as_ascii=False):
    rate, data = wavfile.read(filepath)
    if data.ndim > 1:  # Stereo → mono
        data = data[:, 0]

    bits = ''.join(str(sample & 1) for sample in data)
    if as_ascii:
        chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        return ''.join(chars)
    else:
        return bits

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 signal_lsb_decoder.py <file.wav> [--ascii]")
        sys.exit(1)

    wav_path = sys.argv[1]
    ascii_mode = "--ascii" in sys.argv

    try:
        result = extract_lsb_from_wav(wav_path, as_ascii=ascii_mode)
        print(f"[+] Extracted data:\n{result[:300]}...")
    except Exception as e:
        print(f"[!] Failed: {e}")

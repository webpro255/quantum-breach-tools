#!/usr/bin/env python3
"""
morse_decoder.py - Decode Morse code to ASCII

Usage:
    python3 morse_decoder.py "<morse_code>"

Morse format examples:
- .- .-.. .-.. / -.-- --- ..- .-. / -... .- ... .
- .... . .-.. .-.. ---   .-- --- .-. .-.. -..

Supports `/`, triple space, or single space for separation.
"""

import sys

MORSE_CODE_DICT = {
    '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
    '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J',
    '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O',
    '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T',
    '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y',
    '--..':'Z', '-----':'0', '.----':'1', '..---':'2',
    '...--':'3', '....-':'4', '.....':'5', '-....':'6',
    '--...':'7', '---..':'8', '----.':'9'
}

def decode_morse(code):
    # Normalize: replace triple space or / with word breaks
    code = code.strip().replace('   ', ' / ').replace(' / ', ' / ')
    words = code.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.strip().split()
        decoded_letters = [MORSE_CODE_DICT.get(letter, '?') for letter in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 morse_decoder.py \"<morse_code>\"")
        sys.exit(1)

    morse_input = sys.argv[1]
    result = decode_morse(morse_input)
    print(f"[+] Decoded message: {result}")

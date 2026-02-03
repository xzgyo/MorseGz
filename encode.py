#!/usr/bin/env python3
import os
import sys
import gzip

MORSE_MAP = {
    '0': '_____',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '.',
    'F': '.._.'
}

def get_gz_hex(text: str):
    compressed = gzip.compress(text.encode('utf-8'))
    result = compressed.hex().upper()
    return result

def get_morse_text(text: str):
    encoded = "/".join(MORSE_MAP[char] for char in text.upper())
    return encoded

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_text = sys.argv[1]
    else:
        source_text = input("Source text: ").rstrip('\n')
    if source_text:
        gz_hex = get_gz_hex(source_text)
        sys.stdout.write(f'Gzipped hex:\n{gz_hex}\n')
        morse_text = get_morse_text(gz_hex)
        sys.stdout.write(f'Morse:\n{morse_text}\n')
#!/usr/bin/env python3
import sys
import gzip

MORSE_MAP = {
    '_____': '0',
    '.____': '1',
    '..___': '2',
    '...__': '3',
    '...._': '4', 
    '.....': '5',
    '_....': '6',
    '__...': '7',
    '___..': '8',
    '____.': '9',
    '._': 'A',
    '_...': 'B',
    '_._.': 'C',
    '_..': 'D',
    '.': 'E',
    '.._.': 'F'
}

def morse_to_hex(morse_str):
    parts = morse_str.strip().split('/')
    try:
        return "".join(MORSE_MAP[p] for p in parts if p)
    except KeyError as e:
        sys.stdout.write(f"Error: Invalid Morse code: {e}\n")
        sys.exit(1)

def hex_ungzip(hex_str):
    try:
        compressed_bytes = bytes.fromhex(hex_str)
        return gzip.decompress(compressed_bytes).decode('utf-8')
    except Exception as e:
        return f"Error at hex_ungzip(): {e}"

if __name__ == "__main__":
    mode = "hex"
    raw_input = ""
    args = sys.argv[1:]
    if "-m" in args:
        mode = "morse"
        args.remove("-m")
    if args:
        raw_input = args[0]
    else:
        raw_input = input(f"Input your {'morse code' if mode == 'morse' else 'hex nums'}: ").rstrip('\n')
    if not raw_input:
        sys.exit(0)
    if mode == "morse":
        hex_data = morse_to_hex(raw_input)
    else:
        hex_data = raw_input
    result = hex_ungzip(hex_data)
    sys.stdout.write(f'{result}\n')
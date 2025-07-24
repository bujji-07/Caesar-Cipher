# Caesar-Cipher  Caesar Cipher Encoder & Decoder

This project implements a Caesar Cipher for both encoding and decoding messages by shifting letters by a given number of positions.

How It Works

- Each letter is shifted by `N` positions.
- Encoding shifts letters forward.
- Decoding shifts them backward.
- Non-alphabet characters (spaces, punctuation) are preserved.

Input

- `message`: string to encode/decode
- `shift`: integer number of positions to shift
- `decode`: boolean flag (default is `False`)

Output

- Encoded or decoded message

Usage Example

```python
message = "Hello, World!"
encoded = caesar_cipher(message, 3)
decoded = caesar_cipher(encoded, 3, decode=True)

print("Encoded:", encoded)  # Khoor, Zruog!
print("Decoded:", decoded)  # Hello, World!

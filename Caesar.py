def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


message = "Hello, World!"
encoded = caesar_cipher(message, 3)
decoded = caesar_cipher(encoded, 3, decode=True)

print("Encoded:", encoded)
print("Decoded:", decoded)

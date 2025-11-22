def caesar_encrypt(plain_text, shift):
    cipher_text = ''
    for ch in plain_text:
        if ch.isalpha():
            if ch.isupper():
                c = (ord(ch) - 65 + shift) % 26 + 65
                cipher_text += chr(c)
            else:
                c = (ord(ch) - 97 + shift) % 26 + 97
                cipher_text += chr(c)
        else:
            cipher_text += ch
    return cipher_text

def caesar_decrypt(cipher_text, shift):
    plain_text = ''
    for ch in cipher_text:
        if ch.isalpha():
            if ch.isupper():
                p = (ord(ch) - 65 - shift + 26) % 26 + 65
                plain_text += chr(p)
            else:
                p = (ord(ch) - 97 - shift + 26) % 26 + 97
                plain_text += chr(p)
        else:
            plain_text += ch
    return plain_text

# User input
plain = input("Enter plain text: ")
shift = int(input("Enter shift value: "))

cipher = caesar_encrypt(plain, shift)
print("\nCaesar Cipher:")
print("Plain Text:", plain)
print("Cipher Text:", cipher)
print("Decrypted Text:", caesar_decrypt(cipher, shift))
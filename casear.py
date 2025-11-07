def caesar_encrypt(plain_text, shift=3):
    plain_text = plain_text.upper().replace(" ", "")
    cipher_text = ''
    for ch in plain_text:
        if ch.isalpha():
            c = (ord(ch) - 65 + shift) % 26 + 65
            cipher_text += chr(c)
        else:
            cipher_text += ch
    return cipher_text

def caesar_decrypt(cipher_text, shift=3):
    cipher_text = cipher_text.upper().replace(" ", "")
    plain_text = ''
    for ch in cipher_text:
        if ch.isalpha():
            p = (ord(ch) - 65 - shift + 26) % 26 + 65
            plain_text += chr(p)
        else:
            plain_text += ch
    return plain_text

plain = input("Enter plain text: ")
shift = int(input("Enter shift value: "))

cipher = caesar_encrypt(plain, shift)
print("\nCaesar Cipher:")
print("Plain Text:", plain)
print("Cipher Text:", cipher)
print("Decrypted Text:", caesar_decrypt(cipher, shift))

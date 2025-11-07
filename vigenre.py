def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    key = key.upper()
    cipher_text = ''
    key_index = 0

    for ch in plain_text:
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(key[key_index % len(key)]) - 65
            c = (p + k) % 26
            cipher_text += chr(c + 65)
            key_index += 1
        else:
            cipher_text += ch  
    return cipher_text


def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper().replace(" ", "")
    key = key.upper()
    plain_text = ''
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            c = ord(ch) - 65
            k = ord(key[key_index % len(key)]) - 65
            p = (c - k + 26) % 26
            plain_text += chr(p + 65)
            key_index += 1
        else:
            plain_text += ch
    return plain_text


plain_text = input("Enter plain text: ")
key = input("Enter key: ")

cipher_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(cipher_text, key)

print("\n")
print("Plain Text:    ", plain_text)
print("Key:           ", key)
print("Cipher Text:   ", cipher_text)
print("Decrypted Text:", decrypted_text)

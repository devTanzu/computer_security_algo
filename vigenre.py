def vigenere_encrypt(plain_text, key):
    key = key.upper()
    cipher_text = ''
    key_index = 0

    for ch in plain_text:
        if ch.isalpha():
            is_upper = ch.isupper()
            p = ord(ch.upper()) - 65
            k = ord(key[key_index % len(key)]) - 65
            c = (p + k) % 26
            encrypted_char = chr(c + 65)
            cipher_text += encrypted_char if is_upper else encrypted_char.lower()
            key_index += 1
        else:
            cipher_text += ch  # preserve non-letters (spaces, punctuation)
    return cipher_text


def vigenere_decrypt(cipher_text, key):
    key = key.upper()
    plain_text = ''
    key_index = 0

    for ch in cipher_text:
        if ch.isalpha():
            is_upper = ch.isupper()
            c = ord(ch.upper()) - 65
            k = ord(key[key_index % len(key)]) - 65
            p = (c - k + 26) % 26
            decrypted_char = chr(p + 65)
            plain_text += decrypted_char if is_upper else decrypted_char.lower()
            key_index += 1
        else:
            plain_text += ch
    return plain_text


# -------------------------
# USER INPUThe
# -------------------------
plain_text = input("Enter plain text: ")
key = input("Enter key: ")

cipher_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(cipher_text, key)

print("\nPlain Text:    ", plain_text)
print("Key:           ", key)
print("Cipher Text:   ", cipher_text)
print("Decrypted Text:", decrypted_text)
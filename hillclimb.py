import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

def matrix_mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det %= mod
    det_inv = pow(det, -1, mod) 
    inv_matrix = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % mod
    return inv_matrix

def hill_encrypt(plain_text, key_matrix):
    pt = plain_text.upper().replace(" ", "")
    n = key_matrix.shape[0]
    while len(pt) % n != 0:
        pt += 'X'
    cipher = ''
    for i in range(0, len(pt), n):
        block = np.array([char_to_num(c) for c in pt[i:i+n]])
        enc = key_matrix.dot(block) % 26
        cipher += ''.join(num_to_char(int(x)) for x in enc)
    return cipher

def hill_decrypt(cipher_text, key_matrix):
    ct = cipher_text.upper().replace(" ", "")
    n = key_matrix.shape[0]
    key_inv = matrix_mod_inverse(key_matrix, 26)
    plain = ''
    for i in range(0, len(ct), n):
        block = np.array([char_to_num(c) for c in ct[i:i+n]])
        dec = key_inv.dot(block) % 26
        plain += ''.join(num_to_char(int(round(x))) for x in dec)
    return plain

n = int(input("Enter the size of key matrix (n x n): "))
print(f"Enter {n*n} numbers row-wise for key matrix (space separated):")
key_values = list(map(int, input().split()))
key_matrix = np.array(key_values).reshape(n, n)

plaintext = input("Enter plaintext: ")

ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted = hill_decrypt(ciphertext, key_matrix)

print("\nKey matrix:\n", key_matrix)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)

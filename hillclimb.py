import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n, is_upper):
    ch = chr((n % 26) + ord('A'))
    return ch if is_upper else ch.lower()

def matrix_mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det %= mod
    det_inv = pow(det, -1, mod)

    cofactors = np.zeros(matrix.shape, dtype=int)
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
            cofactors[r][c] = ((-1)**(r+c)) * int(round(np.linalg.det(minor)))

    adj = cofactors.T
    inv_matrix = (det_inv * adj) % mod
    return inv_matrix


def hill_encrypt(plain_text, key_matrix):
    spaces = [i for i, c in enumerate(plain_text) if c == " "]   # save space index
    cases = [c.isupper() for c in plain_text if c != " "]        # save case info
    clean = [c for c in plain_text if c != " "]                  # remove spaces for block processing

    pt = ''.join(c.upper() for c in clean)
    n = key_matrix.shape[0]

    # padding
    while len(pt) % n != 0:
        pt += 'X'
        cases.append(True)

    cipher_chars = []
    idx = 0

    for i in range(0, len(pt), n):
        block = np.array([char_to_num(c) for c in pt[i:i+n]])
        enc = key_matrix.dot(block) % 26
        for x in enc:
            cipher_chars.append(num_to_char(int(x), cases[idx]))
            idx += 1

    # restore spaces
    for s in spaces:
        cipher_chars.insert(s, " ")

    return ''.join(cipher_chars)


def hill_decrypt(cipher_text, key_matrix):
    spaces = [i for i, c in enumerate(cipher_text) if c == " "]
    cases = [c.isupper() for c in cipher_text if c != " "]
    clean = [c for c in cipher_text if c != " "]

    ct = ''.join(c.upper() for c in clean)
    n = key_matrix.shape[0]
    key_inv = matrix_mod_inverse(key_matrix, 26)

    plain_chars = []
    idx = 0

    for i in range(0, len(ct), n):
        block = np.array([char_to_num(c) for c in ct[i:i+n]])
        dec = key_inv.dot(block) % 26
        for x in dec:
            plain_chars.append(num_to_char(int(x), cases[idx]))
            idx += 1

    # restore spaces
    for s in spaces:
        plain_chars.insert(s, " ")

    return ''.join(plain_chars)


# USER INPUT
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
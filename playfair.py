def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    matrix_5x5 = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return matrix_5x5

def find_position(matrix, char):
    if char == 'J':
        char = 'I'
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j
    return None

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = ''
        if i + 1 < len(plain_text):
            b = plain_text[i + 1]
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b if b else 'X'))

    cipher_text = ''
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:  
            cipher_text += matrix[r1][(c1 + 1) % 5]
            cipher_text += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  
            cipher_text += matrix[(r1 + 1) % 5][c1]
            cipher_text += matrix[(r2 + 1) % 5][c2]
        else:  
            cipher_text += matrix[r1][c2]
            cipher_text += matrix[r2][c1]
    return cipher_text

# User input
key = input("Enter key: ")
plain = input("Enter plain text: ")

print("\nPlayfair Cipher:")
print("Plain Text:", plain)
print("Cipher Text:", playfair_encrypt(plain, key))

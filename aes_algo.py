from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

def encrypt(plaintext: bytes, key: bytes) -> bytes:
    """Encrypts plaintext using AES in ECB mode and returns Base64 encoded ciphertext."""
    cipher = AES.new(key, AES.MODE_ECB)        # Create AES cipher in ECB mode
    padded = pad(plaintext, AES.block_size)    # Pad plaintext to block size (16 bytes)
    ciphertext = cipher.encrypt(padded)        # Encrypt the padded plaintext
    return base64.b64encode(ciphertext)        # Return Base64 encoded ciphertext

# --- Example usage ---
key = get_random_bytes(16)                    # Generate random 16-byte AES key
plaintext = b"Hello, AES Encryption!"        # Plaintext must be bytes

encrypted_data = encrypt(plaintext, key)
print("Encrypted (Base64):", encrypted_data.decode())

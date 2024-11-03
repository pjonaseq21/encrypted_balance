from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import hashlib

def get_key(key_string: str) -> bytes:
    return hashlib.sha256(key_string.encode()).digest()

def decrypt_file(file_path: str, key: str):
    key_bytes = get_key(key)  
    with open(file_path, 'rb') as f:
        iv = f.read(16)  
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()

    return plaintext




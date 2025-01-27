import sys
import os

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def derive_key(password, salt, length=32):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=length,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt_file(filename, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(filename, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_filename = f"{filename}.enc"
    with open(encrypted_filename, 'wb') as f:
        f.write(salt + iv + ciphertext)

    print(f"File encrypted successfully: {encrypted_filename}")


def decrypt_file(encrypted_filename, password):
    with open(encrypted_filename, 'rb') as f:
        data = f.read()

    salt, iv, ciphertext = data[:16], data[16:32], data[32:]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()

    decrypted_filename = encrypted_filename.replace(".enc", ".dec")
    with open(decrypted_filename, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted successfully: {decrypted_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <encrypt|decrypt> <filename> <password>")
        sys.exit(1)

    action, filename, password = sys.argv[1], sys.argv[2], sys.argv[3]

    if action.lower() == "encrypt":
        encrypt_file(filename, password)
    elif action.lower() == "decrypt":
        decrypt_file(filename, password)
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)


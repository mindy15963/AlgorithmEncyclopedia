# 카멜리아 (Camellia)
# 대칭형 블록 암호화 알고리즘으로, 128비트 블록 크기와 128비트, 192비트, 256비트 키 크기를 지원한다.

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

def generate_key():
    password = b'mysecretpassword'
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)
    return key

def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

def encrypt_camellia(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = pad(plaintext)
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_camellia(key, ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpad(padded_data)
    return plaintext

key = generate_key()
plaintext = input('평문 입력 : ').encode()

ciphertext = encrypt_camellia(key, plaintext)
print("암호문 : ", ciphertext)

decrypted_text = decrypt_camellia(key, ciphertext)
print("복호문 : ", decrypted_text.decode())
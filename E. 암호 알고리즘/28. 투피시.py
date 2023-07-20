# 투피시 (Twofish)
# 블록 크기가 128비트, 키 크기가 최대 256비트인 대칭 키 블록 암호이다.

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def generate_key(password, salt):
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    return key

def pad(data):
    length = 16 - (len(data) % 16)
    return data + (chr(length) * length).encode()

def unpad(data):
    return data[:-data[-1]]

def encrypt(key, plaintext):
    salt = get_random_bytes(8)
    key = generate_key(key, salt)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext))
    return salt + cipher.iv + ciphertext

def decrypt(key, ciphertext):
    salt = ciphertext[:8]
    iv = ciphertext[8:24]
    ciphertext = ciphertext[24:]
    key = generate_key(key, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))
    return plaintext

key = b'Sixteen byte key'
plaintext = input('평문 입력 : ').encode()
ciphertext = encrypt(key, plaintext)
decrypted_text = decrypt(key, ciphertext)

print("평문 : ", plaintext)
print("암호문 : ", ciphertext)
print("복호문 : ", decrypted_text)
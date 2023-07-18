# 블로피시 (Blowfish)
# 데이터 암호화 표준(DES)와 국제 데이터 암호화 알고리즘을 대신하여 사용되는 암호화 알고리즘이다.

from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)

def encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_plaintext = pad(plaintext, 8)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, 8)
    return plaintext

message = input('평문 입력 : ').encode()
ciphertext = encrypt(message, key)
decrypted_message = decrypt(ciphertext, key)

print("평문 : ", message)
print("암호문 : ", ciphertext)
print("복호문 : ", decrypted_message.decode())
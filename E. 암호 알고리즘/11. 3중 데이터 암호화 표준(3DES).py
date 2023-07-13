# 3중 데이터 암호화 표준 (3DES, Triple DES)
# 각 데이터 블록에 DES 암호 알고리즘을 세 번 적용하는 대칭 키 블록 암호이다.

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_3des(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, 8))
    return ciphertext

def decrypt_3des(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), 8)
    return plaintext

key = get_random_bytes(24)

plaintext = input('평문 입력 : ').encode()

ciphertext = encrypt_3des(key, plaintext)
print("암호문 : ", ciphertext)

decrypted_text = decrypt_3des(key, ciphertext)
print("복호문 : ", decrypted_text)
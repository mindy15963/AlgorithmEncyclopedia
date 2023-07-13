# RC4 (Rivest Cipher 4)
# SSL/TLS나 네트워킹 프로토콜에서 자주 사용되는 스트림 암호기법이다.

from Crypto.Cipher import ARC4

def rc4_encrypt(data, key):
    cipher = ARC4.new(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

def rc4_decrypt(encrypted_data, key):
    cipher = ARC4.new(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

key = b'0123456789ABCDEF'
data = input('평문 입력 : ').encode()

encrypted_data = rc4_encrypt(data, key)
decrypted_data = rc4_decrypt(encrypted_data, key)

print("암호문 : ", encrypted_data)
print("복호문 : ", decrypted_data)
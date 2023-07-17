# RSA 암호화 (RSA key cryptosystem)
# 현재 SSL/TLS에 가장 많이 사용되는 공개키 암호화 알고리즘이다.

import rsa

(public_key, private_key) = rsa.newkeys(2048)

plaintext = input('평문 입력 : ').encode()
ciphertext = rsa.encrypt(plaintext, public_key)
decrypted_text = rsa.decrypt(ciphertext, private_key)

print("평문 : ", plaintext)
print("암호문 : ", ciphertext)
print("복호문 : ", decrypted_text)
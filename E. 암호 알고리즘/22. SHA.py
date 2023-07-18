# SHA (Secure Hash Algorithm)
# 미국 NSA가 제작하고 미국 국립표준기술연구소(NIST)에서 표준으로 채택한 암호학적 해시 함수이다.

import hashlib

def sha256_hash_string(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode('utf-8'))
    return sha256_hash.hexdigest()

message = input('문자열 입력 : ')

sha256_string = sha256_hash_string(message)

print("문자열의 SHA-256 해시 : ", sha256_string)
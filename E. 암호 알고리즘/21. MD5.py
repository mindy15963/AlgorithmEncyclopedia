# MD5 (Message-Digest algorithm 5)
# 임의의 길이의 값을 입력받아서 128비트 길이의 해시값을 출력하는 알고리즘이다.

import hashlib

def md5_hash_string(message):
    md5_hash = hashlib.md5()
    md5_hash.update(message.encode('utf-8'))
    return md5_hash.hexdigest()

message = input('문자열 입력 : ')

md5_string = md5_hash_string(message)

print("문자열의 MD5 해시 : ", md5_string)
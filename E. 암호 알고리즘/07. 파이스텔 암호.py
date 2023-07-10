# 버넘 암호 (Feistel Cipher)
# 암호화 방식이 특정 계산 함수의 반복으로 이루어진 무작위 발생 글자들로 이루어진 블록 암호 알고리즘이다.

import feistelcipher.FeistelCipher as fc
import feistelcipher.CryptFunctions as cfs
plain=int(input('평문 입력 : '))
funcList = cfs.CryptFunctions()
cipher = fc.FeistelCipher(funcList)
enc = cipher.encrypt(plain)
print('암호문 : ',enc)
dec = cipher.decrypt(enc)
print('복호문 : ',dec)
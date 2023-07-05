# 카이사르 암호 (Caesar Cipher)
# 각 알파벳 문자를 두 문자 건너의 세 번째 문자로 치환되는 방식이다.

from caesarcipher import CaesarCipher
plain=input('평문 입력 : ')
cipher1=CaesarCipher(plain)
print('암호문 : ',cipher1.encoded)
for i in range(0,26):
    cipher2=CaesarCipher(cipher1.encoded,offset=i)
    print(f'복호문 {i+1} : ',cipher2.decoded)
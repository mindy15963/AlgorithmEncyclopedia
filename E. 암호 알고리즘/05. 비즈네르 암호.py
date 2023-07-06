# 비즈네르 암호 (Vigenere Cipher)
# 다중 단일 문자 치환 암호법의 한 종류로 키워드를 이용한 암호법이다.

from kryptor.vigenere_cipher import VigenereCipher
plain=input('평문 입력 : ')
obj = VigenereCipher()
en=obj.encrypt(plain,'key')
print('암호문 : ',en)
de=obj.decrypt(en,'key')
print('복호문 : ',de)
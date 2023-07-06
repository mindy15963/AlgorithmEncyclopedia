# 버넘 암호 (Vernam Cipher)
# 반복되지 않는 문자들로 이루어진 무작위 발생 글자들로 이루어진 키를 사용해 구현하는 알고리즘이다.

from kryptor.vernam_cipher import VernamCipher
plain=input('평문 입력 : ')
obj = VernamCipher()
key=input('키 입력 : ')
en=obj.encrypt(plain,key)
print('암호문 : ',en)
de=obj.decrypt(en,key)
print('복호문 : ',de)
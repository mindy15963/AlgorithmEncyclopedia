# 플레이페어 암호 (Playfair Cipher)
# 평문에 등장하는 문자의 빈도와 암호문에서 사용되는 문자의 빈도를 다르게 만드는 알고리즘이다.

from kryptor.playfair_cipher import PlayfairCipher
plain=input('평문 입력 : ')
obj = PlayfairCipher()
en=obj.encrypt(plain, "key")
print('암호문 : ',en)
de=obj.decrypt(en, "key")
print('복호문 : ',de)
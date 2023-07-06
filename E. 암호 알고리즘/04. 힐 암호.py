# 힐 암호 (Hill Cipher)
# 선형 대수학을 기반으로 하는 다중 문자 대체 암호법이다.

from kryptor.hill_cipher import HillCipher
plain=input('평문 입력 : ')
obj = HillCipher()
key=[list(map(int, input(f'{_+1}차원 키 입력 : ').split())) for _ in range(2)]
en=obj.encrypt(plain,key)
print('암호문 : ',en)
de=obj.decrypt(en,key)
print('복호문 : ',de)
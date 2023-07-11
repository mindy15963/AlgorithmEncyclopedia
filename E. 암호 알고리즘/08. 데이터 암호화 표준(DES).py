# 데이터 암호화 표준 (DES, Data Encryption Standard)
# 64비트 평문을 64비트 암호문으로 암호화하는 대칭키 암호 알고리즘이다.

from Crypto.Cipher import DES
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

key = input('키 입력 : ').encode()
text1 = input('평문 입력 : ')

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text.encode())

print('암호문 : ',encrypted_text)
print('복호문 : ',des.decrypt(encrypted_text))
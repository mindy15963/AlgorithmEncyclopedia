# 고급 암호화 표준 (AES, Advanced Encryption Standard)
# 미국 표준 기술 연구소에 의해서 연방 정보 처리 표준으로 지정된 암호화 방식이며 NSA에 의해 1급 비밀에 사용할 수 있도록 승인된 암호화 알고리즘이다.

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
BS=16

key = input('키 입력 : ')
plain = input('평문 입력 : ')

aes = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
encrypted_text = aes.encrypt(pad(plain.encode(), BS))

print('암호문 : ',encrypted_text)
print('복호문 : ',aes.decrypt(encrypted_text))
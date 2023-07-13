# 의사 난수 생성기 (PNRG, Pseudo Random Number Generator)
# 많은 양의 난수 발생이 필요할 때 확률 및 통계, 응용프로그램을 위해서 사용되는 랜덤 발생기이다.
# 여기서는 CTR 모드를 다룬다.

from Crypto.Cipher import AES
from Crypto.Util import Counter

def generate_key():
    key = b'Sixteen byte key'
    return key

def generate_nonce():
    nonce = b'Nonce123'
    return nonce

def generate_prng(key, nonce):
    counter = Counter.new(64, nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    return cipher

def generate_random_bytes(cipher, size):
    random_bytes = cipher.encrypt(b'\x00' * size)
    return random_bytes

key = generate_key()
nonce = generate_nonce()

prng = generate_prng(key, nonce)

random_bytes = generate_random_bytes(prng, 16)

print("결과값 : ", random_bytes)

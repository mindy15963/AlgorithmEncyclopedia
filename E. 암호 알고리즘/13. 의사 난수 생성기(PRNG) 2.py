# 의사 난수 생성기 (PNRG, Pseudo Random Number Generator)
# 많은 양의 난수 발생이 필요할 때 확률 및 통계, 응용프로그램을 위해서 사용되는 랜덤 발생기이다.
# 여기서는 OFB 모드를 다룬다.

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key():
    key = b'Sixteen byte key'
    return key

def generate_iv():
    iv = get_random_bytes(16)
    return iv[:16]

def generate_prng(key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    return cipher

def generate_random_bytes(cipher, size):
    random_bytes = cipher.encrypt(bytes(size))
    return random_bytes

key = generate_key()
iv = generate_iv()

prng = generate_prng(key, iv)

random_bytes = generate_random_bytes(prng, 16)

print("결과값 : ", random_bytes)
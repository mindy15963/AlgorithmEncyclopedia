# 타원 곡선 디피-헬만 알고리즘 (ECDH, Elliptic Curve Diffie-Hellman)
# 타원 곡선 암호 알고리즘을 활용한 키 교환 기법이다.

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def perform_ecdh_key_exchange(private_key, public_key):
    shared_key = private_key.exchange(ec.ECDH(), public_key)
    return shared_key

private_key1 = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key1 = private_key1.public_key()

private_key2 = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key2 = private_key2.public_key()

shared_key1 = perform_ecdh_key_exchange(private_key1, public_key2)
shared_key2 = perform_ecdh_key_exchange(private_key2, public_key1)

print("공유된 키 동일 여부 : ", shared_key1 == shared_key2)
# 전자서명 알고리즘 (DSA, Digital Signature Algorithm)
# 디지털 서명을 생성하고 검증하기 위한 알고리즘이다.

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generate_dsa_signature(private_key, message):
    hash_obj = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

def verify_dsa_signature(public_key, message, signature):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_obj, signature)
        return True
    except ValueError:
        return False

message = input('평문 입력 : ').encode()
key = DSA.generate(1024)

private_key = key
public_key = key.publickey()

signature = generate_dsa_signature(private_key, message)
is_valid = verify_dsa_signature(public_key, message, signature)

print("디지털 서명 유효성 : ", is_valid)
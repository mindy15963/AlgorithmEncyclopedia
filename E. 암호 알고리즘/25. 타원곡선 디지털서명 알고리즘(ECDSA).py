# 타원곡선 디지털서명 알고리즘 (ECDSA,lliptic Curve Digital Signature Algorithm)
# 타원곡선암호를 전자서명에 접목시킨 암호 알고리즘이다.

from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generate_ecdsa_signature(private_key, message):
    hash_obj = SHA256.new(message)
    signer = DSS.new(private_key, 'deterministic-rfc6979')
    signature = signer.sign(hash_obj)
    return signature

def verify_ecdsa_signature(public_key, message, signature):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(public_key, 'deterministic-rfc6979')
    try:
        verifier.verify(hash_obj, signature)
        return True
    except ValueError:
        return False

message = input('평문 입력 : ').encode()
key = ECC.generate(curve='P-256')

private_key = key
public_key = key.public_key()

signature = generate_ecdsa_signature(private_key, message)
is_valid = verify_ecdsa_signature(public_key, message, signature)

print("디지털 서명 유효성 : ", is_valid)
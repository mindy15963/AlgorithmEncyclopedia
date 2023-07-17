# 타원곡선 암호 (Elliptic Curve Cryptography)
# 타원곡선 이론에 기반한 공개 키 암호 방식이다.

from ecdsa import SigningKey

private_key = SigningKey.generate()
public_key = private_key.get_verifying_key()

message = input('평문 입력 : ').encode()
signature = private_key.sign(message)

is_valid = public_key.verify(signature, message)

print("서명 검증 결과 : ", is_valid)
# 디피-헬만 알고리즘 (Diffie-Hellman Algorithm)
# 두 사용자가 사전에 어떤 비밀 교환 없이도 공통키를 교환하게 해주는 알고리즘이다.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

private_key = parameters.generate_private_key()

public_key = private_key.public_key()

shared_key = private_key.exchange(public_key)

print("공유 키 : \n", shared_key)
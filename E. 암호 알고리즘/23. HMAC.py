# HMAC (Hash-based Message Authentication Code)
# 키를 이용하여 메시지의 무결성을 검증하는 메시지 인증 코드이다.

import hashlib
import hmac

def hmac_sha256(key, message):
    hmac_hash = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
    return hmac_hash.hexdigest()

message = input('문자열 입력 : ')
key = "SecretKey"

hmac_sha256_hash = hmac_sha256(key, message)

print("HMAC-SHA256 해시 : ", hmac_sha256_hash)
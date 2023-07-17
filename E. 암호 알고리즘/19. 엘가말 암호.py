# 엘가말 암호 (ElGamal encryption)
# 타헤르 엘가말이 1985년에 고안한, 디피-헬만 키 교환을 바탕으로 한 공개 키 암호 방식이다.

from fastecdsa import curve, keys

private_key, public_key = keys.gen_keypair(curve.P256)

message = input('평문 입력 : ').encode()
k = keys.gen_private_key(curve.P256)
K = k * curve.P256.G
c1 = k * curve.P256.G

c2 = k * curve.P256.G + int.from_bytes(message, 'big') * K

decrypted_message = c2 - private_key * c1
decrypted_message = decrypted_message.x.to_bytes((decrypted_message.x.bit_length() + 7) // 8, 'big')

print("평문 : ", message)
print("암호문 : ", c2)
try:
    decrypted_message = decrypted_message.decode('utf-8')
    print("복호문 : ", decrypted_message)
except UnicodeDecodeError:
    print("복호문 : ", decrypted_message)
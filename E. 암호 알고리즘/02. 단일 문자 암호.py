# 단일 문자 암호 (Monoalphabetic Cipher)
# 항상 문자에 대해서는 같은 문자로 치환하는 방식이다.

import random
alpha = "abcdefghijklmnopqrstuvwxyz"
def encrypt(original, key=None):
    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)
    new = []
    for letter in original:
        new.append(key[alpha.index(letter)])
    return ["".join(new), key]

def decrypt(cipher, key=None):
    if key is not None:
        new = []
        for letter in cipher:
            new.append(alpha[key.index(letter)])

        return "".join(new)
plain=input('평문 입력 : ')
e = encrypt(plain, None)
print('암호문 : ',e)
print('복호문 : ',decrypt(e[0], e[1]))
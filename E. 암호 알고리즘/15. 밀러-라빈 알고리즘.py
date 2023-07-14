# 밀러-라빈 알고리즘 (Miller-Rabin Algorithm)
# 입력으로 주어진 수가 소수인지 아닌지 판별하는 알고리즘이다.

import secrets

def miller_rabin(n, k):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

primes = [n for n in range(1, 101) if miller_rabin(n, k=5)]
print("소수 : ", primes)
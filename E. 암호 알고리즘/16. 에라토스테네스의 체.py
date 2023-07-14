# 에라토스테네스의 체 (Sieve of Eratosthenes)
# 소수들을 대량으로 빠르고 정확하게 구하는 방법이다.

from sympy import sieve

def is_prime(n):
    return n in sieve

primes = [n for n in range(1, 101) if is_prime(n)]
print("소수 : ", primes)
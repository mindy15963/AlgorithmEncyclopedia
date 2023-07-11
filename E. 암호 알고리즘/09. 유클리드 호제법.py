# 유클리드 호제법 (Euclidean Algorithm)
# 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘의 하나이다.

import math as m

n1=int(input('값 1 입력 : '))
n2=int(input('값 2 입력 : '))

print('결과값 : ',m.gcd(n1,n2))
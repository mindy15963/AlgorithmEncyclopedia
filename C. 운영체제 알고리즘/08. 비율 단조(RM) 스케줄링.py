# 비율 단조(Rate-Monotonic) 스케줄링
# 선점형, 선점이 가능한 우선순위를 사용하여 스케줄링하는 알고리즘이다.

import math as m

e=[0.0 for _ in range(20)]
p=[0.0 for _ in range(20)]
ut=0.0
u=0.0
x=0.0
y=0.0

n=int(input("프로세스의 개수 입력 : "))

for i in range(0,n):
    e[i]=float(input(f"프로세스 {i+1}의 실행 시간 입력 : "))
    p[i]=float(input(f"프로세스 {i+1}의 실행 주기 입력 : "))

for i in range(0,n):
    x=e[i]/p[i]
    ut+=x

y=float(n)
y=y*((m.pow(2.0,1/y))-1)
u=y

if ut<u:
    print(f"{ut} < {u}: 시스템은 확실하게 예약 가능합니다.")
else:
    print("예약에 부적합합니다.")
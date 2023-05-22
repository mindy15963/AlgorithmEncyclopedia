# 다단계 큐(Multilevel Queue) 스케줄링
# 커널 내의 준비 큐를 여러 개의 큐로 분리하여 큐 사이에도 우선순위를 부여하는 스케줄링 알고리즘이다.

p=[0 for _ in range(20)]
bt=[0 for _ in range(20)]
su=[0 for _ in range(20)]
wt=[0 for _ in range(20)]
tat=[0 for _ in range(20)]

n=int(input("프로세스의 개수 입력 : "))

for i in range(0,n):
    p[i] = i
    bt[i]=int(input(f"프로세스 {i+1}의 실행 시간 입력 : "))
    su[i]=int(input("시스템 프로세스는 0을, 사용자 프로세스는 1을 입력 : "))
 
for i in range(0,n):
    for k in range(i+1,n):
        if(su[i] > su[k]):
            p[i],p[k]=p[k],p[i]
            bt[i],bt[k]=bt[k],bt[i]
            su[i],su[k]=su[k],su[i]
wtavg = wt[0] = 0
tatavg = tat[0] = bt[0]

for i in range(1,n):
    wt[i] = wt[i-1] + bt[i-1]
    tat[i] = tat[i-1] + bt[i]
    wtavg += wt[i]
    tatavg += tat[i]
 
print("| 프로세스 | 시스템/사용자 프로세스 | 실행 시간 | 대기 시간 | 반환 시간 |")
for i in range(0,n):
    print(f"| {p[i]} | {su[i]} | {bt[i]} | {wt[i]} | {tat[i]} |")
print(f"평균 대기 시간 : {wtavg/n}")
print(f"평균 반환 시간 : {tatavg/n}")
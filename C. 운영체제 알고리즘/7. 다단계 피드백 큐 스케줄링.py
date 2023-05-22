# 다단계 피드백 큐(Multilevel Feedback Queue) 스케줄링
# 다단계 큐 스케줄링에서 한 단계 발전된 방식으로, 1962년 페르난도 J. 코바토가 처음 개발했다.

from dataclasses import dataclass
import string as s

@dataclass
class process:
    name: str=''
    AT: int=0
    BT: int=0
    WT: int=0
    TAT: int=0
    RT: int=0
    CT: int=0

Q1=[process() for _ in range(10)]
Q2=[process() for _ in range(10)]
Q3=[process() for _ in range(10)]

k=0
r=0
time=0
tq1=5
tq2=8
flag=0

n=int(input("프로세스의 개수 입력 : "))

for i,c in zip(range(0,n),s.ascii_uppercase[:n]):
    Q1[i].name=c
    Q1[i].AT, Q1[i].BT=map(int, input(f"프로세스 {Q1[i].name}의 도착 시간 및 실행 시간 입력 : ").split())
    Q1[i].RT=Q1[i].BT
 
temp=process()

for i in range(0,n):
    for j in range(i+1,n):
        if Q1[i].AT>Q1[j].AT:
            Q1[i],Q1[j]=Q1[j],Q1[i]

time=Q1[0].AT

print("시간 단위가 5인 라운드 로빈을 통한 첫번째 큐에서의 프로세스")
print("| 프로세스 | 응답 시간 | 대기 시간 | 반환 시간 |")

for i in range(0,n):
    if Q1[i].RT<=tq1:
        time+=Q1[i].RT
        Q1[i].RT=0
        Q1[i].WT=time-Q1[i].AT-Q1[i].BT
        Q1[i].TAT=time-Q1[i].AT
        print(f"| {Q1[i].name} | {Q1[i].BT} | {Q1[i].WT} | {Q1[i].TAT} |")
    else:
        Q2[k].WT=time
        time+=tq1
        Q1[i].RT-=tq1
        Q2[k].BT=Q1[i].RT
        Q2[k].RT=Q2[k].BT
        Q2[k].name=Q1[i].name
        k+=1
        flag=1
        
if flag==1:
    print("시간 단위가 8인 라운드 로빈을 통한 두번째 큐에서의 프로세스")
    print("| 프로세스 | 응답 시간 | 대기 시간 | 반환 시간 |")
    for i in range(0,k):
        if Q2[i].RT<=tq2:
            time+=Q2[i].RT
            Q2[i].RT=0
            Q2[i].WT=time-tq1-Q2[i].BT
            Q2[i].TAT=time-Q2[i].AT
            print(f"| {Q2[i].name} | {Q2[i].BT} | {Q2[i].WT} | {Q2[i].TAT} |")
        else:
            Q3[r].AT=time
            time+=tq2
            Q2[i].RT-=tq2
            Q3[r].BT=Q2[i].RT
            Q3[r].RT=Q3[r].BT
            Q3[r].name=Q2[i].name
            r+=1
            flag=2
if flag==2:
    print("FCFS를 통한 3번째 큐에서의 프로세스")
    for i in range(0,r):
        if i==0:
            Q3[i].CT=Q3[i].BT+time-tq1-tq2
        else:
            Q3[i].CT=Q3[i-1].CT+Q3[i].BT
            
for i in range(0,r):
    Q3[i].TAT=Q3[i].CT
    Q3[i].WT=Q3[i].TAT-Q3[i].BT
    print(f"| {Q3[i].name} | {Q3[i].BT} | {Q3[i].WT} | {Q3[i].TAT} |")
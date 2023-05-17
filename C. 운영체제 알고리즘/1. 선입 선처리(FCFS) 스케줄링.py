# 선입 선처리(FCFS) 스케줄링
# 먼저 자원 사용을 요청한 프로세스에게 자원을 할당해 주는 방식의 스케줄링 알고리즘이다.

n= int(input("프로세스의 개수 입력 : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("프로세스 "+str(i+1)+"의 도착 시간 입력 : "))
    b = int(input("프로세스 "+str(i+1)+"의 실행 시간 입력 : "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
 
ET = []
for i in range(len(d)):
    if(i==0):
        ET.append(d[i][1][1])
 
    else:
        ET.append(ET[i-1] + d[i][1][1])
 
TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])
 
WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])
 
avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)

avg_TAT = 0
for i in TAT:
    avg_TAT +=i
avg_TAT = (avg_TAT/n)
 
print("| 프로세스 | 도착 시간 | 실행 시간 | 완료 시간 | 반환 시간 | 대기 시간 |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
print("평균 대기 시간 : ",avg_WT)
print("평균 반환 시간 : ",avg_TAT)
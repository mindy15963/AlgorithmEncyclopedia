# 최단 마감 우선(Earliest Deadline First) 스케줄링
# 선점 가능한 동적 우선순위 정책을 이용하여 주기 프로세스들을 스케줄링 하는 알고리즘이다.

tasks=[]
n=int(input('프로세스의 개수 입력 : '))

for i in range(n):
    tasks.append([])
    tasks[i].append(i+1)
    tasks[i].append(int(input(f'프로세스 {i+1}의 실행 시간 입력 : ')))
    tasks[i].append(int(input(f'프로세스 {i+1}의 주기 시간 입력 : ')))
    tasks[i].append(int(input(f'프로세스 {i+1}의 마감 시간 입력 : ')))
    tasks[i].append(int(input(f'프로세스 {i+1}의 도착 시간 입력 : ')))

print(tasks)

u=0

for i in range(n):
    u+=float(tasks[i][1]/tasks[i][2])

print(f"활용도 : {u}")

if u>1:
    print("작업을 수행할 수 없습니다.")

else:
    lcm=1
    temp_p=[]
    for i in range(n):
        temp_p.append(tasks[i][2])

    print(temp_p)
    i=2
    while i <= max(temp_p):
        counter=0
        for j in range(n):
            if temp_p[j]%i==0:
                counter=1
                temp_p[j]/=i

        if counter==1:
            lcm=lcm*i
        else:
            i+=1

    print("최소공배수 : ",lcm)

    i=0
    instances=[]
    for i in range(n):
        j=1
        while 1:
            if j*tasks[i][2]<=lcm:
                instances.append([tasks[i],j*tasks[i][2]])
                j+=1
            else:
                break

    for i in range(len(instances)):
        print(instances[i])

    for i in range(len(instances)):
        tmp = instances[i].copy()
        k = i
        while k > 0 and tmp[1] < instances[k-1][1]:
            instances[k] = instances[k - 1].copy()
            k -= 1
        instances[k] = tmp.copy()

    for i in range(len(instances)):
        print(instances[i])
    
    timeLeft=[]

    for i in range(n):
        if tasks[i][4]==0:
            timeLeft.append(tasks[i][1])
        else:
            timeLeft.append(int(0))

    timeLine=[]
    time=0
    
    while time<lcm:
        for i in range(n):
            if time>1 and ((time%tasks[i][2]==0 and time>tasks[i][4]) or time==tasks[i][4]):
                timeLeft[i]=tasks[i][1]
        anyrun=0
        for j in range(len(instances)):
            if j==0 and timeLeft[instances[j][0][0]-1]>0:
                timeLine.append(instances[j][0][0])
                timeLeft[instances[j][0][0]-1]-=1
                anyrun=1
                if timeLeft[instances[j][0][0]-1]==0:
                    instances.pop(j)
                break

            elif j>0 and instances[j][1]==instances[0][1]:
                if timeLeft[instances[j][0][0]-1]>0:
                    tmp=instances[j].copy()
                    instances[j]=instances[0].copy()
                    instances[0]=tmp.copy()
                    time-=1
                    anyrun=1
                    break
            elif j>0 and timeLeft[instances[j][0][0]-1]>0:
                timeLine.append(instances[j][0][0])
                timeLeft[instances[j][0][0]-1]-=1
                anyrun=1
                if timeLeft[instances[j][0][0]-1]==0:
                    instances.pop(j)
                break

        if anyrun==0:
            timeLine.append(0)

        time+=1

    mn=0
    mx=0

    for i in range(lcm):
        if i>0 and timeLine[i]!=timeLine[i-1]:
            mx=i
            print(mn,"",mx,"", "["+str(timeLine[i-1])+"]")
            mn=i
        if i==lcm-1:
            mx=lcm
            print(mn,"",mx,"", "["+str(timeLine[i])+"]")

    for i in range(len(instances)):
            print(instances[i])
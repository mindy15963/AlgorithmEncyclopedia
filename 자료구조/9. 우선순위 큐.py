# 우선순위 큐 (Priority Queue)
# 데이터마다 우선순위를 지정하여, 정렬된 큐로, 우선순위 높은 순으로 출력하는 자료구조이다.

import queue as q
dq=q.PriorityQueue()
pn=int(input('우선순위 큐에 입력할 값의 개수 입력 : '))
for i in range(pn):
    pqna,pqnb=map(int,input('우선순위 큐에 입력할 값 입력 : ').split())
    dq.put((pqna,pqnb))
gn=int(input('우선순위 큐에서 출력할 값의 개수 입력 : '))
for i in range(gn):
    print(dq.get())
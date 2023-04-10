# 큐 (Queue)
# 일반적인 큐 자료구조
import queue as q
dq=q.Queue()
pn=int(input('큐에 입력할 값의 개수 입력 : '))
for i in range(pn):
    qn=int(input('큐에 입력할 값 입력 : '))
    dq.put(qn)
gn=int(input('큐에서 출력할 값의 개수 입력 : '))
for i in range(gn):
    print(dq.get())
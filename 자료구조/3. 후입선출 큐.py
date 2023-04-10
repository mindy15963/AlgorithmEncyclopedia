# 후입선출 큐 (LIFO Queue)
# 나중에 입력된 데이터가 먼저 출력되는 구조(스택과 동일)
import queue as q
dq=q.LifoQueue()
pn=int(input('후입선출 큐에 입력할 값의 개수 입력 : '))
for i in range(pn):
    qn=int(input('후입선출 큐에 입력할 값 입력 : '))
    dq.put(qn)
gn=int(input('후입선출 큐에서 출력할 값의 개수 입력 : '))
for i in range(gn):
    print(dq.get())
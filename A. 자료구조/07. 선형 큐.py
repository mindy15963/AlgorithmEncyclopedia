# 선형 큐 (Linear Queue)
# 양 방향에서 입력과 출력이 진행되는 자료구조를 뜻한다.
# 선입선출(First In First Out, FIFO) 구조로 가장 먼저 들어온 데이터가 가장 먼저 리턴, 출력된다는 뜻이다.
from queue import Queue
q=Queue()
pn=int(input('큐에 입력할 값의 개수 입력 : '))
for i in range(pn):
    qn=int(input('큐에 입력할 값 입력 : '))
    q.put(qn)
gn=int(input('큐에서 출력할 값의 개수 입력 : '))
for i in range(gn):
    print(q.get())
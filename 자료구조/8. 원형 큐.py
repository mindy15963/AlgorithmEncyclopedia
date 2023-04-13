# 원형 큐 (Circular Queue)
# 선형 큐의 문제점을 보완하고자 나온 자료구조이다.
# 큐를 직선 형태로 놓는 것보다 원형으로 생각해서 큐를 구현하는 것으로 큐를 원형으로 생각해야되기 때문에 모듈러 연산(나머지 연산)을 해야 한다.

from collections import deque
dcq=list(map(int,input('삽입할 값 입력 : ').split()))
ml=int(input('원형 큐의 최대 길이 입력 : '))
cq=deque(dcq,maxlen=ml)
cqa=int(input('원형 큐에 삽입할 값 입력 : '))
cq.append(cqa)
cqe=int(input('원형 큐에 추가로 삽입할 값 입력 : '))
cq.extend([cqe])

print(cq)
print(cq.pop()) #dequeue
print(cq)
cq.rotate(-1)
print(cq)
print(cq.pop()) #dequeue
print(cq)
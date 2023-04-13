# 데크 (Deque)
# 양쪽에서 모두 삽입/인출이 가능한 스택과 큐의 특징을 모두 갖고 있는 자료구조이다.

from collections import deque
n = int(input('입력할 값의 갯수 입력 : '))
deq = deque()
 
for i in range(n):
    v = int(input('입력할 값 입력 : '))
    deq.append(v)

print(deq)
while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())
print(deq.pop())
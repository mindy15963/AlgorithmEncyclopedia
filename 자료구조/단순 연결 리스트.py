# 단순 연결 리스트 (Singly Linked List)
# 동적 메모리 할당을 이용해 노드들을 한 방향으로 연결하여 리스트를 구현한 자료구조
# 삽입이나 삭제 시 항목들의 이동이 필요없음.
# 하지만 항목을 탐색하려면 항상 첫 노드부터 원하는 노드를 찾을 때까지 차례로 방문하는 순차탐색을 이용해야 함.

import llist as ll
  
# 단순 연결 리스트 생성
sll = list(input('입력할 값 입력 : ').split())
lst = ll.sllist(sll)
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()
  
# 값 추가 및 삽입
v1=input('추가할 값 입력 : ')
lst.append(v1)
na1=int(input('값을 삽입할 색인 번호 입력 : '))
node = lst.nodeat(na1)

v2=input('추가할 값 입력 : ')
lst.insertafter(v2,node)
  
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()
  
# 값 삭제
# 리스트의 마지막 값 삭제
lst.pop()
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()
  
# 특정 값 삭제
na2=int(input('값을 삭제할 색인 번호 입력 : '))
node = lst.nodeat(na2)
lst.remove(node)
print(lst)
print(lst.first)
print(lst.last)
print(lst.size)
print()
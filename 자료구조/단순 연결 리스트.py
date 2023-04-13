# 단순 연결 리스트 (Singly Linked List)
# 각 노드 당 한 개의 포인터가 있고 포인터는 다음 노드의 위치를 가르키며 테일은 가장 마지막이므로 다음을 가리키는 포인터를 갖지 않는다.

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
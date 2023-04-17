# 단순 연결 리스트 (Singly Linked List)
# 각 노드 당 한 개의 포인터가 있고 포인터는 다음 노드의 위치를 가르키며 테일은 가장 마지막이므로 다음을 가리키는 포인터를 갖지 않는다.

from dstructure.SLL import SLL
  
obj=SLL()
n=int(input('입력할 값의 개수 입력 : '))
for i in range(n):
    v=input('입력할 값 입력 : ')
    obj.insert(v)
obj.getnodes()
obj.print()

'''
rv=input('삭제할 값 입력 : ')
obj.delete(rv)
obj.getnodes()
obj.print()
'''

# 맨 앞쪽 값 삭제
'''
obj.delete_f()
obj.getnodes()
obj.print()
'''

# 맨 뒷쪽 값 삭제
'''
obj.delete_l()
obj.getnodes()
obj.print()
'''
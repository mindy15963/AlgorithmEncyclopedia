# 이중 연결 리스트 (Singly Linked List)
# 단일 연결 리스트는 포인터를 한 개 가지고 있어 다음 노드만 가리킬 수 있었다면 이중 연결 리스트는 포인터를 두 개 가지고 있어 이전 노드와 다음 노드를 가리킨다.

from dstructure.DLL import DLL
  
obj=DLL()
n=int(input('입력할 값의 갯수 입력 : '))
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
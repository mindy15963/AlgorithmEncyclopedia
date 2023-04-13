# 원형 단순 연결 리스트 (Singly Circular Linked List)
# 단일 연결 리스트의 테일에 포인터가 추가된 형태로 테일의 포인터는 헤더를 가르켜 원형이 되도록 한다.

from dstructure.SCLL import SCLL
  
obj=SCLL()
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
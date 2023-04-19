# 레드 블랙 트리 (Red-black tree)
# 자가 균형 이진 탐색 트리의 일종으로, 노드에 색깔 속성이 붙은 트리이다.

from redblacktree import rbtree

data=list(map(int,input('배열 입력 : ').split()))
rbt=rbtree(data)

print('레드 블랙 트리 결과값 : \n',rbt)

irbt=int(input('삽입할 노드 입력 : '))
rbt.insert(irbt)
print('레드 블랙 트리 결과값 : \n',rbt)

rrbt=int(input('삭제할 노드 입력 : '))
rbt.remove(rrbt)
print('레드 블랙 트리 결과값 : \n',rbt)
# AVL 트리 (AVL tree)
# 스스로 균형을 잡는 이진 탐색 트리이다.

from TreeAVL.AVL import AVL

data=list(map(int,input('배열 입력 : ').split()))
avlt=AVL(data)
print('AVL 트리 결과값 (회전 전) : \n',avlt)
avlt.BalanceTree()
print('AVL 트리 결과값 (회전 후) : \n',avlt)

iavlt=int(input('삽입할 노드 입력 : '))
data.append(iavlt)
avlt=AVL(data)
print('AVL 트리 결과값 (회전 전) : \n',avlt)
avlt.BalanceTree()
print('AVL 트리 결과값 (회전 후) : \n',avlt)
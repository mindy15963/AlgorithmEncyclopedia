# 힙 트리 (Heap Tree)
# 여러 개의 값 중에서 가장 크거나 작은 값을 빠르게 찾기 위해 만든 이진 트리로 힙(Heap)이라고도 부른다.
# 최대 힙 (Max Heap)
# 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리이다.

import heapq as h
from binarytree import *

tree=list(map(int,input('노드에 입력할 값 입력 : ').split()))
for i in range(len(tree)):
    tree[i]*=-1
h.heapify(tree)
heap_tree = build(tree)
print('결과물 :\n')
heap_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',heap_tree.values)
print('중위 순회 결과 :', heap_tree.inorder)
print('전위 순회 결과 :', heap_tree.preorder)
print('후위 순회 결과 :', heap_tree.postorder)
print('레벨 순서 순회 결과 :', heap_tree.levelorder)
print('노드의 개수 :', heap_tree.size)
print('트리의 높이 :', heap_tree.height)

iv=int(input('삽입할 노드 값 입력 : '))
h.heappush(tree,-1*iv)
heap_tree = build(tree)
print('결과물 :\n')
heap_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',heap_tree.values)
print('중위 순회 결과 :', heap_tree.inorder)
print('전위 순회 결과 :', heap_tree.preorder)
print('후위 순회 결과 :', heap_tree.postorder)
print('레벨 순서 순회 결과 :', heap_tree.levelorder)
print('노드의 개수 :', heap_tree.size)
print('트리의 높이 :', heap_tree.height)

print(h.heappop(tree))
heap_tree = build(tree)
print('결과물 :\n')
heap_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',heap_tree.values)
print('중위 순회 결과 :', heap_tree.inorder)
print('전위 순회 결과 :', heap_tree.preorder)
print('후위 순회 결과 :', heap_tree.postorder)
print('레벨 순서 순회 결과 :', heap_tree.levelorder)
print('노드의 개수 :', heap_tree.size)
print('트리의 높이 :', heap_tree.height)
# 이진 탐색 트리 (Binary Search Tree, BST)
# 순서화된 이진 트리로 노드의 왼쪽 자식은 부모의 값보다 작은 값을 가져야 하며 노드의 오른쪽 자식은 부모의 값보다 큰 값을 가져야 한다.

from binarytree import *

nodes=list(input('노드에 입력할 값 입력 : ').split())
for i in range(len(nodes)):
    if nodes[i]=='None':
        nodes[i]=None
    else:
        nodes[i]=int(nodes[i])

binary_search_tree = build(nodes)
print('결과물 :\n')
binary_search_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',binary_search_tree.values)
print('중위 순회 결과 :', binary_search_tree.inorder)
print('전위 순회 결과 :', binary_search_tree.preorder)
print('후위 순회 결과 :', binary_search_tree.postorder)
print('레벨 순서 순회 결과 :', binary_search_tree.levelorder)
print('노드의 개수 :', binary_search_tree.size)
print('트리의 높이 :', binary_search_tree.height)

ii=int(input('삽입할 노드의 인덱스 입력 : '))
iv=int(input('해당 인덱스에 입력할 값 입력 : '))
binary_search_tree[ii]=Node(iv)
print('결과물 :\n')
binary_search_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',binary_search_tree.values)
print('중위 순회 결과 :', binary_search_tree.inorder)
print('전위 순회 결과 :', binary_search_tree.preorder)
print('후위 순회 결과 :', binary_search_tree.postorder)
print('레벨 순서 순회 결과 :', binary_search_tree.levelorder)
print('노드의 개수 :', binary_search_tree.size)
print('트리의 높이 :', binary_search_tree.height)

di=int(input('삭제할 노드의 인덱스 입력 : '))
del binary_search_tree[di]
print('결과물 :\n')
binary_search_tree.pprint(index=True)
print('입력된 이진 탐색 트리 노드 값 :',binary_search_tree.values)
print('중위 순회 결과 :', binary_search_tree.inorder)
print('전위 순회 결과 :', binary_search_tree.preorder)
print('후위 순회 결과 :', binary_search_tree.postorder)
print('레벨 순서 순회 결과 :', binary_search_tree.levelorder)
print('노드의 개수 :', binary_search_tree.size)
print('트리의 높이 :', binary_search_tree.height)
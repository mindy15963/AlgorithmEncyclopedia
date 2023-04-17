# 이진 트리 (Binary Tree)
# 각 노드의 차수(자식 노드)가 2 이하인 트리이다.

from binarytree import build

nodes=list(input('노드에 입력할 값 입력 : ').split())
for i in range(len(nodes)):
    if nodes[i]=='None':
        nodes[i]=None
    else:
        nodes[i]=int(nodes[i])

binary_tree = build(nodes)
print('결과물 :\n')
binary_tree.pprint(index=True)
print('입력된 이진 트리 노드 값 :',binary_tree.values)
print('중위 순회 결과 :', binary_tree.inorder)
print('전위 순회 결과 :', binary_tree.preorder)
print('후위 순회 결과 :', binary_tree.postorder)
print('레벨 순서 순회 결과 :', binary_tree.levelorder)
print('노드의 개수 :', binary_tree.size)
print('트리의 높이 :', binary_tree.height)
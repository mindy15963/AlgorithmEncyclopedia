# 위상 정렬 (Topological sort)
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.

import networkx as nx
import matplotlib.pyplot as plt

nodes=list(input('노드 값 입력 : ').split())
G = nx.DiGraph()
G.add_nodes_from(nodes)
edges=list(tuple(input('엣지 값 입력 : ').split()) for r in range(int(input('엣지의 개수 입력 : '))))
G.add_edges_from(edges)

ts=nx.topological_sort(G)
nx.draw(G, font_weight='bold', with_labels=True)
plt.show()
print('결과 값 : \n',list(ts))
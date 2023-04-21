# 트리나 그래프를 방문 또는 탐색하는 방법이다.

import networkx as nx
import matplotlib.pyplot as plt

nodes=list(input('노드 값 입력 : ').split())
G = nx.DiGraph(name='G')
G.add_nodes_from(nodes)
edges=list(tuple(input('엣지 값 입력 : ').split()) for r in range(int(input('엣지의 개수 입력 : '))))
G.add_edges_from(edges)

sn=input('기준 노드 입력 : ')
bfs = nx.bfs_predecessors(G, source=sn)
bfs = dict(bfs)
nx.draw(G, font_weight='bold', with_labels=True)
plt.show()
print('최단거리 : \n',bfs)
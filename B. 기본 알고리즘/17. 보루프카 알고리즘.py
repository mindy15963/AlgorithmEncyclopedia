# 보루프카 알고리즘 (Borůvka's Algorithm)
# 모든 간선들의 가중치가 서로 상이한 그래프에서 최소 신장 트리(MST)를 찾는 알고리즘이다.

import networkx as nx
import matplotlib.pyplot as plt

nodes=list(input('노드 값 입력 : ').split())
G = nx.Graph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    w=int(input('가중치 입력 : '))
    G.add_edge(d,a,weight=w)
mst = nx.minimum_spanning_tree(G, algorithm="boruvka")
pos = nx.spring_layout(G)
nx.draw(G,pos,font_weight='bold', with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
print('결과 값 : \n',sorted(mst.edges(data=True)))
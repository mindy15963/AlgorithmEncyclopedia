# 크루스칼 알고리즘 (Kruskal Algorithm)
# 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘이다.

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
mst = nx.minimum_spanning_tree(G, algorithm="kruskal")
pos = nx.spring_layout(G)
nx.draw(G,pos,font_weight='bold', with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
print('결과 값 : \n',sorted(mst.edges(data=True)))
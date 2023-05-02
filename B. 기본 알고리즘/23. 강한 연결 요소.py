# 강한 연결 요소 (SCC, Strongly Connected Component)
# 노드들이 서로 자유롭게 이동 가능한 모음집이다.

import networkx as nx

nodes=list(input('노드 값 입력 : ').split())
G = nx.MultiDiGraph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    G.add_edge(d,a)
print('결과 값 : \n',sorted(nx.strongly_connected_components(G)))
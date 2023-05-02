# 방향성 비순환 그래프 (DAG, Directed Acyclic Graph)
# 한 방향으로 이어지지만, 순환은 하지 않는 그래프이다.

import networkx as nx

nodes=list(input('노드 값 입력 : ').split())
G = nx.DiGraph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    w=int(input('가중치 입력 : '))
    G.add_edge(d,a,weight=w)
so=input('출발지 입력 : ')
ta=input('도착지 입력 : ')
dag_sp=nx.shortest_path(G, source=so, target=ta)
dag_length=nx.shortest_path_length(G, source=so, target=ta)
print('결과 값 : \n',dag_sp)
print('최단 거리 : \n',dag_length)
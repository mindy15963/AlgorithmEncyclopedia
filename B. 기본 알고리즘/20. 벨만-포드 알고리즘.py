# 벨만-포드 알고리즘 (Bellman-Ford Algorithm)
# 가중 유향 그래프에서 노드 사이의 최단 경로를 찾는 알고리즘이다.

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
bf_path=nx.bellman_ford_path(G, so, ta)
bf_length=nx.bellman_ford_path_length(G, so, ta)
print('결과 값 : \n',bf_path)
print('최소 거리 : ',bf_length)
# 다익스트라 알고리즘 (Dijkstra Algorithm)
# 음의 가중치가 없는 그래프의 한 정점에서 모든 정점까지의 최단거리를 각각 구하는 알고리즘(최단 경로 문제)이다.

import networkx as nx

nodes=list(input('노드 값 입력 : ').split())
G = nx.MultiDiGraph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    w=int(input('가중치 입력 : '))
    G.add_edge(d,a,weight=w)
so=input('출발지 입력 : ')
ta=input('도착지 입력 : ')
d_path=nx.dijkstra_path(G, so, ta)
d_length=nx.dijkstra_path_length(G, so, ta)
print('결과 값 : \n',d_path)
print('최단 거리 : ',d_length)
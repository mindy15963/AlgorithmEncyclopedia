# A* 알고리즘 (A*(A Star) Algorithm)
# 출발 꼭짓점에서부터 목표 꼭짓점까지 가는 최단 경로를 찾아내는 휴리스틱 기반의 그래프 탐색 알고리즘이다.

import networkx as nx

nodes=list(input('노드 값 입력 : ').split())
G = nx.DiGraph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    w=float(input('가중치 입력 : '))
    G.add_edge(d,a,weight=w)
so=input('출발지 입력 : ')
ta=input('도착지 입력 : ')
as_path=nx.astar_path(G, so, ta)
as_length=nx.astar_path_length(G, so, ta)
print('결과 값 : \n',as_path)
print('최단 거리 : ',as_length)
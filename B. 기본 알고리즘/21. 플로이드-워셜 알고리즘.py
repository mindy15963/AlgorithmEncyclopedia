# 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
# 그래프에서 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘이다.

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
fwp,fwd = nx.floyd_warshall_predecessor_and_distance(G)
fw_path=nx.reconstruct_path(so,ta,fwp)
print('결과 값 : \n',fw_path)
print('최단 거리 테이블: \n',fwd)
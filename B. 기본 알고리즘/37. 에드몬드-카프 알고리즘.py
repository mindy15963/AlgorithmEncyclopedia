# 에드몬드-카프 알고리즘 (Edmonds-Karp Algorithm)
# 그래프에서 두 정점 사이에 얼마나 많은 유량을 보낼 수 있는지 계산하는 알고리즘이다.

import networkx as nx
from networkx.algorithms.flow import edmonds_karp

nodes=list(input('노드 값 입력 : ').split())
G = nx.DiGraph()
G.add_nodes_from(nodes)
ec=int(input('엣지의 개수 입력 : '))
for i in range(ec):
    d,a=input('엣지 값 입력 : ').split()
    c=float(input('유량 입력 : '))
    G.add_edge(d,a,capacity=c)
so=input('출발지 입력 : ')
ta=input('도착지 입력 : ')
R=edmonds_karp(G,so,ta)
fv = nx.maximum_flow_value(G,so,ta)
print('결과 값 : ',fv)
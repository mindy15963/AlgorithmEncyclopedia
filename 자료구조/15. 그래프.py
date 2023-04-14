# 그래프 (Graph)
# 노드들이 나무 가지처럼 계층적으로 연결된 비선형 자료구조이다.
# 최상위 노드(루트)가 있고 최상위 노드 아래에 다른 하위 노드가 있고 그 하위 노드 안에는 또 다른 하위 노드가 있는 부모와 자식 형태이다.

import matplotlib.pyplot as plt
import networkx as nx

def generate_adjlist_with_all_edges(G, delimiter=" "):
     for s, nbrs in G.adjacency():
        line = str(s) + delimiter
        for t, data in nbrs.items():
                line += str(t) + delimiter
        yield line[: -len(delimiter)]
        
G = nx.Graph()

nodes=list(map(int,input('노드에 입력할 값 입력 : ').split()))

edges=list(tuple(map(int,input('엣지 값 입력 : ').split())) for r in range(int(input('엣지의 개수 입력 : '))))

G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

am=nx.adjacency_matrix(G).todense()
print('인접 행렬 : \n',am)

print('인접 리스트 : \n')
for line in generate_adjlist_with_all_edges(G):
    print(line)
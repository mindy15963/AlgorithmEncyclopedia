# Union-Find
# 상호 배타적으로 이루어진 집합을 효율적으로 표현하기 위해 만들어진 자료구조이다.
n, m = list(map(int, input('집합의 개수와 연산의 개수 입력 : ').split()))
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    x, a, b = list(map(int, input('원하는 연산(0: 합집합, 1: 집합 포함 확인 연산)과 원소 값 입력 : ').split()))
    if not x:
        union(a, b)
    else:
        if find(a) == find(b):
            print("포함된 것이 맞습니다.")
        else:
            print("포함되지 않았습니다.")
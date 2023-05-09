# 동적 계획법 (DP, Dynamic Programming)
# 최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.
# 행렬 경로 문제
m,n=map(int,input('행의 개수와 열의 개수 입력 : ').split())
a=[]
for i in range(n):
    a.append(list(map(int,input('행렬 입력 : '))))
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        elif j==0:
            a[i][j]+=a[i-1][j]
        elif i==0:
            a[i][j]+=a[i][j-1]
        else:
            a[i][j]+=min(a[i-1][j],a[i][j-1])
print('결과값 : ',a[n-1][m-1])
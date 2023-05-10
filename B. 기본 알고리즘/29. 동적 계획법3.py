# 동적 계획법 (DP, Dynamic Programming)
# 최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.
# 행렬 곱셈 순서 문제
def matrix_chain(n): 
    for d in range(1, n): 
        for i in range(n - d):
            j = i + d
            dp[i][j] = min([dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1] for k in range(i, j)])
    return dp[0][-1]

n = int(input('행렬의 개수 입력 : '))
mat = [list(map(int, input('행렬 입력 : ').split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

print('결과값 : ',matrix_chain(n))
# 배열 (Array)
# 데이터를 나열하고 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# 장점: 빠른 접근 가능 (첫 데이터의 위치에서 상대적인 위치로 데이터 접근 가능 (인덱스)
# 단점: 데이터의 추가/삭제가 어려움 (크기가 고정되어있음)

# 1차원 배열(리스트)
data1=list(map(int,input('1차원 정수 배열 입력 : ').split()))
string1=input('1차원 문자열 배열 입력 : ')
d1n=int(input('원하는 1차원 정수 배열의 색인 입력 : '))
s1n=int(input('원하는 1차원 문자열 배열의 색인 입력 : '))
print(data1[d1n])
print(string1[s1n])

# 2차원 배열
n=int(input('배열의 갯수 입력 : '))
data2=[list(map(int,input('2차원 정수 배열 입력 : ').split())) for _ in range(n)]
d2na,d2nb=map(int,input('원하는 2차원 정수 배열의 색인 입력 : ').split())
print(data2[d2na][d2nb])
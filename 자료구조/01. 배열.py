# 배열 (Array)
# 동일한 타입의 데이터들을 저장(배열이 "int"타입인 경우 정수 요소만 저장 가능)하며, 고정된 크기를 가지고 있다.
# 인덱싱이 되어 있어 인덱스 번호로 데이터에 접근할 수 있다. (인덱스를 지정하여 접근하기 때문에 모든 요소에 빠르게 접근 가능하다.)

# 1차원 배열(리스트)
data1=list(map(int,input('1차원 정수 배열 입력 : ').split()))
string1=input('1차원 문자열 배열 입력 : ')
d1n=int(input('원하는 1차원 정수 배열의 색인 입력 : '))
s1n=int(input('원하는 1차원 문자열 배열의 색인 입력 : '))
print(data1[d1n])
print(string1[s1n])

# 2차원 배열
n=int(input('배열의 개수 입력 : '))
data2=[list(map(int,input('2차원 정수 배열 입력 : ').split())) for _ in range(n)]
d2na,d2nb=map(int,input('원하는 2차원 정수 배열의 색인 입력 : ').split())
print(data2[d2na][d2nb])
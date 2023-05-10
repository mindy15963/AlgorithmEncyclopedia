# 동적 계획법 (DP, Dynamic Programming)
# 최적화 이론의 한 기술이며, 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.
# 최장 공통 부분 순서 문제
import pylcs as pl
x=input('첫번째 문자열 입력 : ')
y=input('두번째 문자열 입력 : ')
print('결과값 : ',pl.lcs(x,y))
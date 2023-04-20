# 이진 탐색 (Binary Search)
# 정렬된 리스트에서 탐색 범위를 절반씩 좁혀 나가며 빠르게 탐색하는 방법이다.

import bisect as bs
data=list(map(int,input('배열 입력 : ').split()))
x=int(input('인덱스를 찾을 값 입력 : '))
bsl=bs.bisect_left(data,x)
print('반환된 인덱스 값 : ',bsl)
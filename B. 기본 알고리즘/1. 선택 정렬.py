# 선택 정렬 (Selection Sort)
# 데이터 배열에서 가장 작은 데이터를 선택하여 앞으로 보내는 정렬이다.

import sorting as so

data=list(map(int,input('배열 입력 : ').split()))
result=so.selection(data)
print('선택 정렬 결과 값 : ',result)
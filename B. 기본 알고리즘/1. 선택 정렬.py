# 선택 정렬 (Selection Sort)
# 데이터 배열에서 가장 작은 데이터를 선택하여 앞으로 보내는 정렬이다.

data=list(map(int,input('배열 입력 : ').split()))
for i in range(len(data) - 1):
    min_idx = i
    for j in range(i + 1, len(data)):
        if data[j] < data[min_idx]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i]
    print(data)
print('선택 정렬 결과 값 : ',data)
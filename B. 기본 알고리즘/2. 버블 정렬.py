# 버블 정렬 (Bubble Sort)
# 옆에 있는 데이터와 비교하여 더 작은 값을 앞으로 보내는 정렬이다.

data=list(map(int,input('배열 입력 : ').split()))
for i in range(len(data) - 1, 0, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
        print(data)
    print(data)
print('버블 정렬 결과 값 : ',data)
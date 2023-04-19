# 삽입 정렬 (Insertion Sort)
# 정렬 범위를 1칸씩 확장해나가면서 새롭게 정렬 범위에 들어온 값을 기존 값들과 비교하여 알맞은 자리에 꼽아주는 알고리즘이다.

data=list(map(int,input('배열 입력 : ').split()))
for end in range(1, len(data)):
    for i in range(end, 0, -1):
        if data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
    print(data)
print('삽입 정렬 결과 값 : ',data)
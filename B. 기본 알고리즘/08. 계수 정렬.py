# 계수 정렬 (Counting Sort)
# 숫자들간 비교를 하지 않고 정렬을 하는 알고리즘이다.

data=list(map(int,input('배열 입력 : ').split()))

count = [0] * (max(data) + 1)

for num in data:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(data))

for num in data:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1
    print(result)

print('계수 정렬 결과 값 : ',result)
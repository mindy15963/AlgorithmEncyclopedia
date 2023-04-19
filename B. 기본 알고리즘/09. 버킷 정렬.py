# 버킷 정렬 (Bucket Sort)
# 정렬되지 않은 자료를 버킷이라는 단위 기억 장소에 여러 그룹으로 정렬하고 버킷별 키 값에 따라 다시 정렬하는 알고리즘이다.

def bucketSort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = round(j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
        print(array)
        
    return array

data=list(map(float,input('배열 입력 : ').split()))
print('버킷 정렬 결과 값 : ',bucketSort(data))
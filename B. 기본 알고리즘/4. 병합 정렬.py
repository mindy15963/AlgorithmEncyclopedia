# 병합 정렬 (Merge Sort)
# 분할 정복 기법과 재귀 알고리즘을 이용한 정렬 알고리즘이다.

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(arr)
    return merged_arr

data=list(map(int,input('배열 입력 : ').split()))
print('병합 정렬 결과 값 : ',merge_sort(data))
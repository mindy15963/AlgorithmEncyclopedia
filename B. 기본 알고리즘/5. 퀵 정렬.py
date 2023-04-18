# 퀵 정렬 (Quick Sort)
# 병합 정렬과 함께 분할 정복 기법과 재귀 알고리즘을 이용한 정렬 알고리즘이다.
# 평균적으로 가장 좋은 성능르 가져 현장에서 가장 많이 쓰이는 정렬 알고리즘이다.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    print(arr)
    print(lesser_arr)
    print(equal_arr)
    print(greater_arr)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

data=list(map(int,input('배열 입력 : ').split()))
print('병합 정렬 결과 값 : ',quick_sort(data))
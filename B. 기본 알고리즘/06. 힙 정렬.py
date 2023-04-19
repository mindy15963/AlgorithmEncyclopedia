# 힙 정렬 (Heap Sort)
# 힙 트리를 구성해 정렬하는 방법으로, 병합 정렬, 퀵 정렬 못지 않게 빠른 정렬 알고리즘이다.

def heap_sort(array):
    n = len(array)
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            c = r
            print(array)
    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            if (c<j-1) and (array[c] < array[c+1]):
                c += 1
            if (c<j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r=c
            print(array)
    print(array)
    return array

data=list(map(int,input('배열 입력 : ').split()))
print('힙 정렬 결과 값 : ',heap_sort(data))
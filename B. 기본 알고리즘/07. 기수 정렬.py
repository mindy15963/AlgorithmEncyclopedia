# 기수 정렬 (Radix Sort)
# 낮은 자리수부터 비교하여 정렬해 간다는 것을 기본 개념으로 하는 정렬 알고리즘이다.

def countingSort(arr, digit):
    n = len(arr)
    
    output = [0] * (n)
    count = [0] * (10)
    
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    for i in range(1,10):
        count[i] += count[i-1]  
        print(i, count[i])
    
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    for i in range(0,len(arr)): 
        arr[i] = output[i]

def radixSort(arr):
    maxValue = max(arr)
    digit = 1
    while int(maxValue/digit) > 0: 
        countingSort(arr,digit)
        digit *= 10
        print(arr)
    return arr

data=list(map(int,input('배열 입력 : ').split()))
print('기수 정렬 결과 값 : ',radixSort(data))
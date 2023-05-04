# 그리디(욕심쟁이) 알고리즘 (Greedy Algorithm)
# "매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자"라는 모토를 가지는 알고리즘 설계 기법이다.

n=int(input('액수 입력 : '))
count=0 

array=list(map(int,input('주어진 동전 입력 : ').split()))

for coin in array:
    count += n // coin
    n %= coin 

print(count)
# 블룸 필터 (Bloom filter)
# 특정 원소가 집합에 속하는지 검사하는데 사용할 수 있는 확률형 자료구조이다.

from bloom_filter import BloomFilter
bf = BloomFilter(max_elements=1000, error_rate=0.1)
cnt=int(input('입력할 원소의 개수 입력 : '))
for i in range(cnt):
    e=input('입력할 원소 입력 : ')
    bf.add(e)

check_e=input('원하는 원소 입력 : ')
if check_e in bf:
    print('이 원소는 집합에 속해 있습니다.')
else:
    print('이 원소는 집합에 속해 있지 않습니다.')
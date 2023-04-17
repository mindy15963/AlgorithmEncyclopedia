# 해시 테이블 (Hash Table)
# 해시함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료구조이다.
# 데이터의 크기에 관계없이 삽입 및 검색에 매우 효율적이다.

from hashtable import HashTable

fs=int(input('해쉬 테이블의 크기 입력 : '))
ht = HashTable(fs)
for i in range(fs):
    k=input('키 입력 : ')
    v=input('값 입력 : ')
    ht[k]=v
    
print('해쉬 테이블 결과값 : \n',ht.items())

sk=input('원하는 키 입력 : ')
print('입력된 키에 해당되는 값 : ',ht[sk])

dk=input('삭제하고 싶은 키 입력 : ')
ht.delete(dk)
print('해쉬 테이블 결과값 : \n',ht.items())
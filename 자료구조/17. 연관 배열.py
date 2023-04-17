# 연관 배열 (Associative array), 해시 (Hash), 딕셔너리 (Dictionary)
# 배열의 인덱스를 정수뿐만이 아닌 다양한 타입으로 설정한 배열이다.

dict={}
ds=int(input('디렉토리의 크기 입력 : '))
for i in range(ds):
    k=input('키 입력 : ')
    v=input('값 입력 : ')
    dict[k]=v

print('디렉토리 결과 값 : ',dict)
print('디렉토리 키 리스트 : ',dict.keys())
print('디렉토리 값 리스트 : ',dict.values())

sk=input('원히는 키 입력 : ')
if sk in dict:
    print('결과값 : ',dict.get(sk))
else:
    print('입력된 키에 해당된 값이 없습니다.')

dk=input('삭제할 키 입력 : ')
del dict[dk]
print('디렉토리 결과 값 : ',dict)
print('디렉토리 키 리스트 : ',dict.keys())
print('디렉토리 값 리스트 : ',dict.values())
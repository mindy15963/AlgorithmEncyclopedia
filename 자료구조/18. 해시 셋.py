# 해시 셋 (Hash Set)
# 해싱을 기반으로 하는 자료구조로 중복을 허용하지 않는다.

hs=set()

fs=int(input('해시 셋의 값의 개수 입력 : '))
for i in range(fs):
    v=input('값 입력 : ')
    hs.add(v)
    
print('해시 셋 결과값 : \n',hs)

sv=input('원하는 값 입력 : ')
if sv in hs:
    print('해당 값은 해시 셋에 존재합니다.')
else:
    print('해당 값은 해시 셋에 존재하지 않습니다.')

dv=input('삭제하고 싶은 값 입력 : ')
hs.remove(dv)
print('해시 셋 결과값 : \n',hs)
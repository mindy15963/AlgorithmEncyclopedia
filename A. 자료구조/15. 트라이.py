# 트라이 (Trie)
# 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조이다.

from pytrie import StringTrie

t=StringTrie()
arr=list(input('입력할 값 입력 : ').split())
for key in arr:
    t[key] = key
print('트라이 결과 값 : ',t)

prefix=input('접두어 입력 : ')
op=t.values(prefix)

if len(op)>0:
    print("해당 접두어에 속해 있는 값 : ",op)
else:
    print("해당 접두어에 속해있는 값이 없습니다.")
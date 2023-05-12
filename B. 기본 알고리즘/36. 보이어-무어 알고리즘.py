# 보이어-무어 알고리즘 (Boyer-Moore Algorithm)
# 문자열 검색 알고리즘으로써 패턴의 전처리로 얻은 정보를 가지고 패턴을 가능한 많이 이동시켜 텍스트와 비교 횟수를 줄인다.

from pyalgs.algorithms.strings.substring_search import BoyerMoore

s1=input('문자열 1 입력 : ')
s2=input('문자열 2 입력 : ')

ss = BoyerMoore(s2)

print('결과값 : ',ss.search_in(s1))
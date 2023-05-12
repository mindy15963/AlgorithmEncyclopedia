# 라빈-카프 알고리즘 (Rabin-Karp Algorithm)
# 해싱을 사용해서 문자열에서 특정 패턴과 일치하는지 찾아주는 알고리즘이다.

from pyalgs.algorithms.strings.substring_search import RabinKarp

s1=input('문자열 1 입력 : ')
s2=input('문자열 2 입력 : ')

ss = RabinKarp(s2)

print('결과값 : ',ss.search_in(s1))
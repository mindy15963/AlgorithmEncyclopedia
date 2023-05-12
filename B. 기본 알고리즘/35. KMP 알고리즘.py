# KMP 알고리즘 (Knuth-Morris-Pratt Algorithm)
# 문자열 검색을 매우 빠르게 해주는 알고리즘이다.

from pyalgs.algorithms.strings.substring_search import KnuthMorrisPratt

s1=input('문자열 1 입력 : ')
s2=input('문자열 2 입력 : ')

ss = KnuthMorrisPratt(s2)

print('결과값 : ',ss.search_in(s1))
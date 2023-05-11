# 나이브 알고리즘 (Naïve Algorithm)
# 우직한 문자열 검색법으로 1번째부터 m번째 글자까지, 2번째부터 m+1번째 글자까지, 이런 식으로 문자열을 일일이 찾아가면서 탐색한다.
def naive(txt,wrd):
    lt=len(txt)
    lw=len(wrd)
    for i in range(lt-lw+1):
        j=0
        while(j<lw):
            if txt[i+j]==wrd[j]:
                j+=1
            else:
                break
        else:
            print('발견된 위치 : ',i)
t=input('문자열 입력 : ')
w=input('단어 입력 : ')
naive(t,w)
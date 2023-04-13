# 스택 (Stack)
# 한 방향으로만 입력할 수 있으며 구조 중간에 값을 끼어 넣어 저장할 수 없다. 즉, 같은 크기의 자료를 정해진 한 방향으로만 입력, 저장, 삭제가 가능하다.
# 입선출(Last In First Out, LIFO) 구조로 가장 마지막에 들어온 데이터가 가장 먼저 리턴, 삭제된다는 뜻이다.

stack=list(map(int,input('삽입할 값 입력 : ').split()))
print(stack)

av=int(input('스택에 삽입할 값 입력 : '))
stack.append(av)
print(stack)

stack.pop()
print(stack)
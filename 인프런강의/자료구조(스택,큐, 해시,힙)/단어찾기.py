#딕셔너리를 사용하면 편리!
#리스트는 인덱스 번호를 정수만 가능하지만
#딕셔너리는 알파벳 등 가능!

n= int(input())
p = dict() #빈 딕셔너리 생성
for i in range(n):
    word = input()
    #딕셔너리의 키에 접근할 때는 대괄호 사용
    p[word]=1
    
for i in range(n-1):
    word = input()
    p[word]=0
    
for key, val in p.items():#items: 키=값 쌍을 모두 가져옴
    if val==1:
        print(key)
        break

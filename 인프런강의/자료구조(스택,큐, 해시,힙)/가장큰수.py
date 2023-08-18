num, m = map(int, input().split())#m개의 숫자를 제거한다.
num = list(map(int, str(num)))

stack=[]
for x in num:
    #x= 현재들어오는 숫자
    #넣는 놈보다 앞에 애들이 작으면 하나씩 pop해준다.
    #제거하는 걸 반복하는 반복문
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    #만약 작지 않으면 append 한다.
    stack.append(x)
if m!=0: 
    stack = stack[:-m] #제일 앞에서 -m자리 이전까지 짤라버린다.

res=''
for i in range(len(stack)):
    res+=str(stack[i])
print(res)
        
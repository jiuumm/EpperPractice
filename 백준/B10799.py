s=input()
stack = []
cnt=0
for i in range(len(s)):
    if s[i]== '(':
        stack.append('(')
    else: #만약 닫는 괄호라면
        if s[i-1]=='(': #레이저인 경우
            stack.pop()
            cnt+= len(stack)
        else: #레이저는 아닌 경우
            stack.pop() #그 다음부분 다시 시작해야 하므로
            cnt+=1
print(cnt)        
            
             
        
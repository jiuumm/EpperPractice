s=input()
stack=[]
cnt=0

for i in range(len(s)):
    if s[i]=='(':
        stack.append('(')
    else: #만약 닫는 괄호라면 바로 앞이 여는 괄호인지 확인
        if s[i-1]=='(':#바로앞이 여는 괄호면 레이저임
            stack.pop()
            cnt+=len(stack)
        else: #이건 쇠막대기의 끝부분임
            stack.pop()
            cnt+=1
            
print(cnt)
#처음에 오는 0은 무시한다.
s = input()
res=0
for x in s:
    if x.isdecimal(): #x가 0~9숫자라면
        res = res*10+int(x)  

cnt=0
for i in range(1, res+1):
    if res %i==0:
        cnt+=1
print(cnt) 
        

s= input()
res=""
cnt=0

if s[0]=="1": #1로 시작하면
    res+="1"
    
cnt=1

for i in range(len(s)-1):
    if s[i]== s[i+1]: #연속하면
        cnt+=1
    else: #연속하지 않으면 
        res+=chr(ord('A')+cnt-1)
        cnt=1
res+=chr(ord('A')+cnt-1)                
    


print(res)    
            
a=input()
b=input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0)+1 #해당 값이 없으면 0을 return
    
for x in b:
    str2 [x]= str2.get(x,0)+1
    
#두개의 구성이 같은지?
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else: #큰 for문이 정상적으로 다 돈다면
    print("YES")
    


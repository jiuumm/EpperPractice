N= int(input()) #공간의 크기
plan = list(map(str, input().split()))
flag = [1,1]
for i in range(len(plan)):
    if plan[i]=='L':
            flag[1]-=1
            if flag[0]>N or flag[0]<1 or flag[1]>N or flag[0]<1:
                flag[1]+=1
                continue
        # flag[0]+=1
    if plan[i]=='R':
            flag[1]+=1
            if flag[0]>N or flag[0]<1 or flag[1]>N or flag[0]<1:
                flag[1]-=1
                continue    
    if plan[i]=='U':
            flag[0]-=1
            if flag[0]>N or flag[0]<1 or flag[1]>5 or flag[0]<1:
                flag[0]+=1
                continue
    if plan[i]=='D':
            flag[0]+=1
            if flag[0]>N or flag[0]<1 or flag[1]>5 or flag[0]<1:
                flag[0]-=1
                continue
print(flag)
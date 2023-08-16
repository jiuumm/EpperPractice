n=int(input())
data=[]
for i in range(n):
    height,weight = map(int, input().split())
    data.append((height, weight))

data.sort(key = lambda x : (x[0], x[1]), reverse=True)

tmp_lst = []

for i in range(n):
    tmp=1
    max = data[i][1]
    for j in range(i, n):
        if max<data[j][1]:
            max = data[j][1]
            tmp+=1
    tmp_lst.append(tmp)
            
max_cnt=tmp_lst[0]
for i in range(n):
    if tmp_lst[i]>max_cnt:
        max_cnt=tmp_lst[i]
print(max_cnt)
    
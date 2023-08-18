n = int(input())
box = list(map(int, input().split()))
repeat = int(input())

for i in range(repeat):
    max = 0
    min= 101
    maxIdx=minIdx=0
    for j in range(n):
        if box[j]>max:
            max=box[j]
            maxIdx=j
            
        if box[j]<min:
            min= box[j]
            minIdx=j
    box[maxIdx] -= 1
    box[minIdx] += 1

max=0
min=101
for i in range(n):
    if box[i]>max:
        max= box[i]
    if box[i]<min:
        min=box[i]
print(max-min)
        
'''
+Feedback
sort함수를 쓰면 정렬이 되는데 
굳이 왜 이런 짓을...
단, 정렬할 때 조심할 부분이 있다.
정렬을 하다보면 min, max가 바뀔 수 있으므로
sort를 한번 더 써야 한다.
'''
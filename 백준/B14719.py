h,w = map(int, input().split())
block = list(map(int, input().split()))

res=0

for i in range(1, w-1):
    left_max = max(block[:i]) # 1~ (현재 바로 왼쪽)
    right_max = max(block[i+1:]) #(현재 바로 오른쪽)~ 끝까지
    
    tmp = min(left_max, right_max)
    
    if block[i]<tmp:
        res+=tmp-block[i]

print(res)
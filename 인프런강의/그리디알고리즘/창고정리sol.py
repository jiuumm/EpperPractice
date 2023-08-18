n = int(input())
box = list(map(int, input().split()))
repeat = int(input())

box.sort()

for _ in range(repeat):
    box[0]+=1
    box[-1]-=1
    box.sort() #이부분이 놓치기 쉬운 부분
print(box[-1]-box[0])
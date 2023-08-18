import heapq as hq
import sys 
input= sys.stdin.readline
n= int(input()) #연산의 개수
a=[]

for _ in range(n):
    x = int(input())
    if x==0: #x가 0이라면 
        if len(a)==0:
            print(0)
        else:
            print(hq.heappop(a))
    else: #x가 자연수
        hq.heappush(a, x)
        
         
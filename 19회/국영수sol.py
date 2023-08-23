import sys
input = sys.stdin.readline

def solution(lst):
    #x는 리스트의 한 요소를 말한다.
    lst.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )
    for i in range(len(lst)):
        print(lst[i][0])

if __name__== '__main__':
    n= int(input())
    lst = []
    for i in range(n):
        lst.append(input().split())
    solution(lst)
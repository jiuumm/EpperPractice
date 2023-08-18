'''
재귀함수 -> 스택을 이용
재귀함수: 반복문의 효과를 낳을 수 있다.
'''
import sys

def DFS(x):
    if x>0: 
        DFS(x-1)
        print(x)
    else:
        return
 
if __name__ == "__main__": #main함수이므로 여기서부터 시작
    n= int(input())
    DFS(n)
    
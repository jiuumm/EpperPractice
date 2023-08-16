#회문 문자열 검사할 때 대소문자를 구분하지 않는다.

n= int(input())
for i in range(n):
    s = input()
    s= s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
            
    
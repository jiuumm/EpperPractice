def check(group):
    cnt=len(group)
    for i in range(len(group)):
        s=group[i]
        for j in range(len(s)-1):
            if s[j+1] != s[j]:
                if s[j] in s[j+1:]:
                    cnt-=1
                    break
    return cnt

if __name__== '__main__':
    n= int(input())
    group=[]
    for _ in range(n):
        group.append(input())
    print(check(group))
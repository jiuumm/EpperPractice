def solution(lst):
    answer = ""
    lst.sort(key = lambda x: x[1], reverse=True)
    for i in range(len(lst)-1):
        if int(lst[i][1])==int(lst[i+1][1]): #국어점수가 같다면
            if int(lst[i][2])>int(lst[i+1][2]): #영어점수로 판별
                lst[i], lst[i+1]= lst[i+1], lst[i]
                
            elif int(lst[i][2])== int(lst[i+1][2]):#영어점수가 같다면
                if int(lst[i][3])<int(lst[i+1][3]): #수학점수로 판별
                    lst[i], lst[i+1]= lst[i+1], lst[i]
                elif int(lst[i][3])==int(lst[i+1][3]):#수학점수가 같다면
                    continue
                else:
                    continue
            else:
                continue
    print(lst)

if __name__== '__main__':
    n= int(input())
    lst = []
    for i in range(n):
        lst.append(input().split())
    print(solution(lst))
from collections import deque
need= input()
n= int(input())
res = []
for _ in range(n):
    lec = input()
    lecture=  deque()
    for i in range(len(lec)):
        lecture.append(lec[i])
    flag=True
    while lecture:
        #prior을 다시 초기화하는 걸 놓침..
        prior= []
        for i in range(len(need)):
            prior.append(need)
        #prior이 다 비어있지 않는 것도 안되는 걸 놓침
        tmp = lecture.popleft()
        if tmp in prior:
            if tmp!=prior[0]:
                print("NO")
                flag==False
                break
            else:
                prior.pop(0)    
                print(prior)
       
    if flag==True:
        print("YES")              


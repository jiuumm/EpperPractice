from collections import deque

n, m = map(int, input().split())
dq = deque([(idx , val)for idx, val in enumerate(list(map(int, input().split())))])
#m번쨰 환자가 진료를 몇번째로 받는지?
cnt=0 #몇번째로 해당 환자가 진료를 받는 지를 나타내주는 변수

while True:
    flag = False
    tmp = dq.popleft()
    for i in range(len(dq)):
        if tmp[1]<dq[i][1]:#만약 뒤에 더 큰 값이 있다면
            flag= True

    if flag== True:
        dq.append(tmp)
    else: #뒤에 더 큰 값이 없다면
        cnt+=1
        if tmp[0] == m:
            print(cnt)
            break          

            
            
        
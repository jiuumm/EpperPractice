from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq=  deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
        
    else:#위의 for문이 break등으로 중간에 빠져나오지 않았을 때
        if len(dq) ==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
        
                  
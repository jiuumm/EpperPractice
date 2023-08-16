remain = [500,100,50,10,5,1]

n= int(input())
coin= 1000-n
res=0
for x in remain:
    res+=coin //x
    coin=coin % x
print(res)

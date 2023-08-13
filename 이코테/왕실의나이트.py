input_data = input()
#행
row = int(input_data[1])
#열 input_data[0]='a'
column = ord(input_data[0])-ord('a')+1
move_delta = [(-1,-2), (1,-2), (1,2), (-1,2),(-2,-1), (-2,1), (2,-1), (2,1) ]
res=0

for delta in move_delta:
    nrow = row+delta[0]
    ncolumn = column+delta[1]
    if nrow<=8 and nrow>=1 and ncolumn<=8 and ncolumn>=1:
        res+=1
print(res)
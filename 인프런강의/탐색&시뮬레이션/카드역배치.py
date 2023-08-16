card = [0]*20
for i in range(20):
    card[i]= i+1
    
for i in range(10):
    s, e = map(int, input().split())
    ai = s-1
    bi = e-1
    for j in range((bi-ai+1)//2):
        card[ai+j], card[bi-j]= card[bi-j], card[ai+j]
        

print(card)
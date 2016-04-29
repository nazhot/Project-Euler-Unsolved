player1 = []
player2 = []
with open("C:\\Users\\Noah\\Documents\\Project Euler\\p054_poker.txt",'r') as f:
    for line in f:
        num = 0
        for word in line.split():
            if num < 5:
                player1.append(word)
            else:
                player2.append(word)
            num+=1
for x in range(0,4996,5):
    p1_rank = []
    p1_suit = []
    p2_rank = []
    p2_suit = []
    for y in range(5):
        p1_rank.append(player1[x+y][0])
        p1_suit.append(player1[x+y][1])
        p2_rank.append(player1[x+y][0])
        p2_suit.append(player1[x+y][1])
    
            

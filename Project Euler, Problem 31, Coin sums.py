def coin_sums(n):
    total = 0
    coins = n
    coins.sort()
    coin_multipliers = [0]*len(coins)
    greatest = coins[-1]
    print(coin_multipliers)
    for x in range(len(coins)):
        coin_multipliers[x] = int(greatest/coins[x])
    print(coin_multipliers)
    for a in range(coin_multipliers[7]+1):
        for b in range(coin_multipliers[6]+1):
            for c in range(coin_multipliers[5]+1):
                for d in range(coin_multipliers[4]+1):
                    for e in range(coin_multipliers[3]+1):
                        for f in range(coin_multipliers[2]+1):
                            for g in range(coin_multipliers[1]+1):
                                for h in range(coin_multipliers[0]+1):
                                    coin_tot = h*coins[0]+g*coins[1]+f*coins[2]+e*coins[3]+d*coins[4]+c*coins[5]+b*coins[6]+a*coins[7] 
                                    if coin_tot == greatest:
                                        total+=1
                                    elif coin_tot > greatest:
                                        break
    return total
    


                       
print(coin_sums([1,2,5,10,20,50,100,200]))

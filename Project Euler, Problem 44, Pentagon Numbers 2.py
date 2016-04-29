n=1
pent_num={1,5,12,22,35,51}

def add_pent():
    n+=1
    pent_num.append(n*(3*n-1)/2)
    return pent_num

def main_fun():
    for x in range(0,len(pent_num)):
        

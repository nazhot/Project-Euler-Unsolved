from math import sqrt

def nth_prime_number(n):
    f, c, primes = 1, 11, [2, 3, 5, 7]
    while primes[-1] < n:
        root = sqrt(c)

        for prime in primes:
            if not c % prime:  # If c is Composite
                break
            elif prime > root:
                primes.append(c)  # Add Prime to List
                n -= 1
                break

        c += 3 - f
        f = -f

    return primes


def tolient_maximum(n):
    print("Calculating primes...")
    array = nth_prime_number(int(sqrt(n)))
    print("Primes calculated!")
    answer = [0,0]
    for x in range(2,n+1):
        percent = 1
        square = int(sqrt(x))
        number = []
        total = 1
        for y in array:
            if x%y == 0:
                number.append(y)
            elif y > square:
                break
        for w in range(x-1, 1, -1):
            test = False
            if x%w == 0:
                continue
            else:
                for z in array:
                    if w%z == 0 and z in number:
                        break
                    elif z > square:
                        test = True
                        break
                if test:
                    total += 1
        if x/total > answer[0]:
            answer[0] = x/total
            answer[1] = x
        if x%10000 == 0:
            print("%s percent done"%(percent))
            percent+=1
            
    return answer
import time

def multiplier(f):
    result = []
    if len(f) > 2:





def tot_max(n):
    answer = [0,0]
    percent = 1
    array = nth_prime_number(int(sqrt(n)))
    for x in range(2,n+1):
        total = 1
        other = []
        square = int(sqrt(x))
        for y in array:
            if y > int(x/2):
                break
            elif x%y == 0:
                other.append(y)
        col = 0
        for z in range(len(other)):
            temp = other[z]
            length = int(x/temp) - 1
            total += length
            for w in range(z-1,-1,-1):
                col += int(length/other[w])
##                for n in range(1,int(x/temp)):
##                    for w in other[:z]:
##                        if (n*temp)%w == 0:
##                            break
##                    else:
##                        total += 1
                    #n += 1
        print(x, x-total+col, x/(x-(total-col)))
        total = x/(x-(total-col))

        if total > answer[0]:
            answer[0] = total
            answer[1] = x
    return answer
    
    
            

print(tot_max(1000000))





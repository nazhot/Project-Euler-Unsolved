from math import sqrt
def number_spiral_diagonals(percent):
    f, c, primes = 1, 11, [2, 3, 5, 7]
    prime_checker=[2,3,5,7]
    total_primes=0
    total_numbers=1
    number=1
    row=3
    while True:
        for x in range(1,5):
            number+=row-1
            while number>prime_checkers[-1]:
                root = sqrt(c)

                for prime in primes:
                    if not c % prime:  # If c is Composite
                        break
                    elif prime > root:
                        primes.append(c)# Add Prime to List
                        prime_checker.append(c)
                        for item in prime_checker:
                            if 
                        break

                c += 3 - f
                f = -f
            if number in primes:
                total_primes+=1
        total_numbers+=4
        if total_primes/total_numbers<percent:
            print(row)
            break
        else:
            row+=2            
number_spiral_diagonals(.1)

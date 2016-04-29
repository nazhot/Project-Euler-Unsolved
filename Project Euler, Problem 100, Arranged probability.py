from math import sqrt
n=10**12
while True:
    if 4-4*(-n**2+n)>=0:
        b=(2+sqrt(4-4*(-n**2+n)))/4
        if b>0 and b==int(b):
            print(b)
            break
        b=(2-sqrt(4-4*(-n**2+n)))/4
        if b>0 and b==int(b):
            print(b)
            break
    n+=1


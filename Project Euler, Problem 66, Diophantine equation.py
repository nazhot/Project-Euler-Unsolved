def diophantine_equation(maximum):
    answer=[0,0]
    square_list=[4]
    square=3
    while square_list[-1]<maximum:
        square_list.append(square**2)
        square+=1
    D=2
    while D<=maximum:
        if D in square_list:
            D+=1
        else:
            x=1
            y=1
            while True:
                equation=x**2-(D*y**2)
                if equation==1:
                    print("D: %s, x: %s, y: %s" %(D,x,y))
                    D+=1
                    if x>answer[1]:
                        answer=[D,x]
                    break
                elif equation<1:
                    x+=1
                    y=1
                else:
                    y+=1
    print(answer)
        

diophantine_equation(1000)
            

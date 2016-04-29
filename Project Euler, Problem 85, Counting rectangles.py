def counting_rectangles(number_of_rectangles):
    answer=[number_of_rectangles]
    for height in range(1,300):
        for width in range(1,300):
            total=0
            for row in range(height):
                for col in range(width):
                    total+=(height-row)*(width-col)
            if abs(number_of_rectangles-total)<answer[0]:
                answer=[abs(number_of_rectangles-total),row,height,row*height]
    print(answer)
    

counting_rectangles(2000000)

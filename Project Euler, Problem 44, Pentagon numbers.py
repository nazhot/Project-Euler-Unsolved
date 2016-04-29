n = 11
pentagon = [1,5,12,22,35,51,70,92,117,145]
differences = [1,5,12,22,35,51,70,92,117,145]
sums = [1,5,12,22,35,51,70,92,117,145]
lists = [pentagon,differences,sums]
min_diff = 0
start = 1
ans = 100000000000
while True:
    #starting point for adding/subtracting always increasing before first number found, then stays constant until another is found
    if ans == 100000000000:
        min_diff = start
    added = 0
    while pentagon[start]+pentagon[start-1] > sums[-1]: #Make sure that the sum of the top two values of pentagon will be within sums
        pentagon_num = (int(n*(3*n-1)/2))
        pentagon.append(pentagon_num)
        sums.append(pentagon_num)
        differences.append(pentagon_num)
        n+=1
        added += 1
    for second in range(start,-1,-1):
        if second == start:
            differences = list(filter(lambda x: x >= pentagon[start] - pentagon[start-1],differences))
        if min_diff == start-second or pentagon[start]+pentagon[second]<pentagon[start+1]:
            sums = list(filter(lambda x: x >= pentagon[start+1] + pentagon[start+1]-pentagon[start],sums))
            break
        if pentagon[start]+pentagon[second] in sums:
            if pentagon[start] - pentagon[second] in differences:
                min_diff = start-second
                print(min_diff)
                ans = min(pentagon[start] - pentagon[second], ans)
                print(ans)
                break
    if min_diff == 1 and ans != 100000000000:
        break
    start += 1
print(ans)

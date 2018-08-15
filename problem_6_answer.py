def sum_difference():
    mylist = [x for x in range(0,101)]
    sum = 0
    for x in mylist:
        sum = sum + x
        sum1 = sum**2

    sum2 = 0
    mylist2 = [ x**2 for x in range(0,101)]
    for y in mylist2:
        sum2 = sum2 + y

    return sum1 - sum2

print(sum_difference())         

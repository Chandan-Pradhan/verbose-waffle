mylist = [x for x in range(0,1001) if x%3==0 or x%5==0]
sum = 0
for x in mylist:
    sum+= x

print(sum)

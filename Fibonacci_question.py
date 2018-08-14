n1 = 0
n2 = 1
n3 = 0
mylist = [ ]
while n3 < 40000000:
    n3 = n1 + n2
    mylist.append(n3)
    n1 = n2
    n2 = n3
mylist2=[x for x in mylist if x%2==0]
sum =0
for x in mylist2:
    sum = sum + x
print(sum)

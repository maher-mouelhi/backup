x = int(input("enter number"))
l =[]
#1, 1, 2, 3, 5, 8, 13, …)

l.append(1)
l.append(1)
for i in range(0,x-2):
    l.append(l[i]+l[i+1])

print(l)
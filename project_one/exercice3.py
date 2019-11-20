list1 = [1,2,3,4,5,23,32,43,-1,'4']
newlist = []

for i in list1:
    if int(i) < 5 :
        newlist.append(i)
print(newlist)

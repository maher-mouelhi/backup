a = [1, 1, 2, 3, 5,1,1,1 ,8, 13, 21, 34, 55, 89]
c = []

for i in a :
    if i not in c :
        c.append(i)

print(list(set(c)))



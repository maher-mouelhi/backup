num = int(input("plz number !  "))
mlist = list(range(1,num+1))
divisors = []

for i in  mlist:
    if num % i == 0 :
        divisors.append(i)

print("list divisors : ",divisors)
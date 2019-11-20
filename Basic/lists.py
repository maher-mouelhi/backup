mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

#fill lists with data
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

#get data from list by index
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
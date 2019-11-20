#operator with numbers
number = 1+2 * 3 / 4.0
print(number)

remainder = 11%3 #reste modulo
print(remainder)

squared = 7**2 # carre puissance 2
cubed = 2**3 # cube puissance 3
#operator with string
helloworld = "hello" +" "+"world"
print(helloworld)

lotofhellos = "hello" * 10
print(lotofhellos)

#operator with list

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers+even_numbers
print(all_numbers)

listrepeated = ([1,2,3] * 3 )
print(listrepeated)

print("###############ECERCICE###################")

x = object()
y = object()

x_list = [x]*10
x_list = x_list
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" %len(x_list))
print("y_list contains %d objects" %len(y_list))
print("big_list contains %d objects" %len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("almost there ...")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("great...")

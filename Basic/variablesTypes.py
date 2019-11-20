#numbers
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat2 = float(7)
print(myfloat2)

#strings

mystring = 'hello'
mystring2 = "hello2"
print(mystring)
print(mystring2)

mstring = "Don't worry about apostrophes"
print(mstring)

one = 1
two = 2

three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a,b = 3,4
print(a,b)

if mystring == "hello":
    print("String : %s" %mystring)
    print("String : ", mystring)
    print("String : " +mystring)

if isinstance(myfloat,float) and myfloat ==7.0:
    print("Float: %f" %myfloat)
if isinstance(myint,int) and myint == 7:
    print("Int : %d" %myint)
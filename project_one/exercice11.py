def getnumber ():
    x = input("enter a number ")
    return x

def isprime (x):
    if x % 1 == 0 and x % x == 0  :
        if x % 2 != 0:
            print("prime")
        elif x == 1 or x == 2:
            print("prime")
        else:
            print("not prime")

if __name__ == '__main__':
    isprime(getnumber())
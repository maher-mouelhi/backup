# user_name = input("Enter your name:")
# print("hello {name}".format(name=user_name))

number = float("5000")
print(number)
print("tot : " , number/3)

print("{},{}".format("hello","world"))
print("{0},{1},{0}".format("abra","cad"))
print("{0}{1}{0}".format("abra","cad"))
print("{first} {last}".format(first="ali",last="baba"))

variable= 5
print(f"{variable}")
print("{variable}")

print("{a:<10}|{a:^10}|{a:>10}".format(a="test"))
print("{a:-<10}|{a:*^10}|{a:->10}".format(a="test"))

person={"first":"cristiano","last":"Ronaldo"}
print("{p[first]} {p[last]}".format(p=person))

data = range(100)
print("{p[0]}...... {p[99]}".format(p=data))

print("{num:f}".format(num=22/7))
print("{num:0.2f}".format(num=22/7))
print("{num:2e}".format(num=22/7))
print("{num:.1%}".format(num=22/7))
print("{num:g}".format(num=5.1200001))
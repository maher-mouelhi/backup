phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#initialized
phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#remove item
del phonebook["John"]
phonebook.pop("Jack")

print(phonebook)
#add item
phonebook["ALI"] = 33333

if "ALI" in phonebook:
    print("ALI is listed in the phonebook.")
if ("John","Jack") not in phonebook:
    print("John and Jack are not listed in the phonebook.")
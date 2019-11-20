a_list = []
a_dict = {}
a_set = set()


for letter in "Hello World!":
    a_list.append(letter)
    a_set.add(letter)
    a_dict[letter] = len(a_list)

print("LIST : ",a_list) #all item default order

list2 = [letter for letter in "Hello World!"]
set2 = {letter for letter in "Hello World!"}
dict2 = {letter:i for i,letter in enumerate("Hello World!")} # default enumarte key start from 0
dict2 = {letter:i for i,letter in enumerate("Hello World!",1)}

print("L2,S2.D2: ",list2,set2,dict2)

print(a_list==list2,a_dict==dict2,a_set==set2)


print("SET : ",a_set) #unique item not repeated and ordred
print("Dict : ",a_dict) ##unique item not repeated and ordred with key(position) and value

a_list2 = []
for letter in "Hello":
    for letter2 in "World":
        a_list2.append((letter,letter2))

print("a_List2 : ",a_list2)

new_list = []
data = [[1,2],[4,5],[6,7],[9,8]]
for row in data:
    for value in row:
        new_list.append(value)

flattened = [value for row in data for value in row]
multidim = [[value for value in row] for row in data]

print("nested List: ",new_list)
print("flattened",flattened)
print("multidim",multidim)

list_word = []
#list_word=[[word.upper(),word,len(word)]for word in "the dog is nice and the cat too"] #not splited it gives by letter not word
list_word=[[word.upper(),word,len(word)]for word in "the dog is nice and the cat too".split()]
print(list_word)
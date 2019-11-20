print ("=================Start my prog made by MM ====================")
list_session = []
list_session2 = []

item = " ITEMS | ses          :"

with open("sessions.txt") as file:
    lines = file.readlines()
    for line in lines:
        line.split()
        if item in line:
            list_session.append(line)

#parsing and geting session name
for s in list_session:
    name = s.strip(item)
    print(name)
    list_session2.append(name.split())


print("liste  ", list_session)
print("liste sessions : by name ", list_session2)





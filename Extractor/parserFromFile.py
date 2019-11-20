mylines = []
mtype = " TYPE  | ses\n"
mlast = '       |\n'




# Declare an empty list.
with open ('sessions.txt', 'rt') as myfile:    # Open sessions.txt for reading text.
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n')) # strip newline and add to list.

        if myline == mtype:
            #print(myline)
            pass
for element in mylines:
    # For each element in the list,
    pass

my_dict = {'name':'Jack', 'age': 26}
my_dict2 = {'name':'ali', 'age': 555}

list_session = []

list_session.append(my_dict)
list_session.append(my_dict2)

print(list_session)

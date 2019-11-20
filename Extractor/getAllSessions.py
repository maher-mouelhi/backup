start_item = ' TYPE  | ses\n'
end_item = '       |\n'

new_item = ""
list_item = []


with open("sessions.txt") as file:
    lines = file.readlines()

my_iterator = iter(lines)

'''looking for an item = session informations ( name , label and list uprocs'''


def getItemSession():
    global new_item
    while True:
        for line in my_iterator:
            if line == start_item:
                next(my_iterator)
                new_item = next(my_iterator)

            elif line == end_item:
                list_item.append(new_item)
                #print("break")
                break
            new_item += line
        else:
            break
    return list_item


#print(getItemSession())





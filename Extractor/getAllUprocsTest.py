start_item = ' TYPE  | upr\n'
end_item = '==================================================\n'
end_item2 = '==================================================\n\n\n'

end_item_space = '\n'
new_item = ""
list_item = []
list_session = []

with open("uprocs_short2.txt") as file:
    lines = file.readlines()

#print(lines)
my_iterator = iter(lines)

'''get list session then looking for the main uproc for each session then get script name from the uprocs file'''
def getItemUproc():
    global new_item
    global list_item

    while True:
        for line in my_iterator:
            new_item += line

            if line == start_item:
                next(my_iterator)
                new_item = next(my_iterator)

            elif line == end_item:
                script_name = next(my_iterator).splitlines()
                #print(script_name)
                list_item.append(new_item)
                list_item.append(script_name)
                #new_item += line
                #new_item += script_name

                new_item2 = next(my_iterator)
                if new_item2 == end_item:
                    #print(line.splitlines())
                    #print(line)
                    #new_item += new_item2
                    list_item.append(new_item2)
                    #print("break")
                    break
            #new_item += line
            #print(line.splitlines())

        else:
            break
    return list_item

def getItemUproc2():
    global new_item
    global list_item
    while True:
        for line in my_iterator:
            new_item += line
            if line == start_item:
                next(my_iterator)
                new_item = next(my_iterator)
            elif line == end_item :
                mnext = next(my_iterator)
                new_item += mnext
                if mnext == "\n":
                    list_item.append(new_item)
                    print("break")
                    break
        else:
            break
    return list_item

#print(getItemUproc2())
list_uproc = getItemUproc2()

#print(type(list_uproc))
print(len(list_uproc))
#print(str(list_uproc))


for mitem in list_uproc :
   print(mitem)


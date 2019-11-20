start_item = ' TYPE  | upr\n'
end_item = '==================================================\n'
end_item_space = '\n'
new_item = ""
list_item = []
list_session = []

with open("uprocs.txt") as file:
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
            elif line == end_item :
                mnext = next(my_iterator)
                new_item += mnext
                if mnext == "\n":
                    list_item.append(new_item)
                    #print("break")
                    break
        else:
            break
    return list_item



#print(getItemUproc2())
list_uproc = getItemUproc()

#print(type(list_uproc))
#print(len(list_uproc))
#print(str(list_uproc))


#for mitem in list_uproc :
#   print(mitem)
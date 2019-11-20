from getAllUprocs import getItemUproc as mItem
item= ""
list_uprocs = []
uproc_item = " ITEMS | upr          :"
label_item = "       | label        : "
end_item = '=================================================='
script_item = "       | script       :"
#print(mItem())
mscript = ''
for item in mItem():
    #print('------------------------------------------------------')
    #list_uproc = []
    dic_uprocs = {}
    linesItem = str(item).split("\n")

    my_iterator = iter(linesItem)

   # print(type(linesItem))
    #print(type(mItem()))

    for line in my_iterator:
        #print(line.splitlines())

        if line.startswith(uproc_item):
            #print(line)

            uproc_line = line.split(':')
            #print(uproc_line[1])
            uproc_name =  uproc_line[1]
            dic_uprocs['uproc_name'] = uproc_name

        if line.startswith(end_item):
            mnext = next(my_iterator)
            mscript = mnext
            if mnext == "":
                break
        dic_uprocs['script_name'] = mscript

        #print(dic_uprocs)

    list_uprocs.append(dic_uprocs)

    #print('//////////////////////////////////////////////////////')
print(list_uprocs)


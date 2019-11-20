from getAllSessions import getItemSession as mItem

item= ""
list_session = []
session_item = " ITEMS | ses          :"
label_item = "       | label        : "
uprocs_item = "                      | upr  :"

for item in mItem():
    #print('------------------------------------------------------')
    list_uproc = []
    dic_session = {}
    linesItem = str(item).split("\n")
    #print(linesItem)
    for line in linesItem :
        #print(line.splitlines())

        if line.startswith(session_item):
            session_line = line.split(':')
            #print(session_line[1])
            session_name =  session_line[1]
            dic_session['session_name'] = session_name

        if line.startswith(label_item):
            label_line = line.split(':')
            #print(label_line[1])
            label = label_line[1]
            dic_session['label'] = label

        if line.startswith(uprocs_item):
            uproc_line = line.split(':')
            #print(uproc_line[1])
            list_uproc.append(uproc_line[1])
            #print(list_uproc)
            dic_session['list_uproc'] = list_uproc
        #print(dic_session)

    list_session.append(dic_session)

    #print('//////////////////////////////////////////////////////')

#print(list_session)
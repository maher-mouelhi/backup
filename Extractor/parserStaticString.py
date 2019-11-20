my_string0 = ' Command : uxshw ses exp ses=* vses=* lst'
my_string00 = '  TYPE  | ses'
my_string1 = 'ITEMS | ses          : ADPJBANIN'
my_string2 = '      | vses         : 000 '
my_string3 =  '       | label        : Traitement ADPGSI BAN'
my_string04 = '       | list         :'
my_string4 = '                      | upr  : ADP0BANIN'
my_string5 = '                      | upr  : ADP_BANIN'
my_string6 = '                      | upr  : ADP9BANIN'
my_string07 = '       |'

list_uproc = []
# split the string at ':'
session_line = my_string1.split(':')
label_line = my_string3.split(':')
uproc_line1 = my_string4.split(':')
uproc_line2 = my_string5.split(':')
uproc_line3 = my_string6.split(':')

#print( "session_line: " ,session_line)
#print( "label_line: " ,  label_line)

# get the first slice of the list
session_name = session_line [1]
label = label_line [1]
uproc1 = uproc_line1 [1]
uproc2 = uproc_line2 [1]
uproc3 = uproc_line3 [1]


list_uproc.append(uproc1)
list_uproc.append(uproc2)
list_uproc.append(uproc3)

print("==================================================")
#print( "session name: " + session_name)
#print( "label: " + label)
#print( "list uprocs : " , list_uproc)
list_session = {'session_name':session_name ,'label' : label , 'list_uprocs': list_uproc }

print( list_session)










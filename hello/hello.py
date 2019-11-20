file = open("mfile.json", 'r')
data = file.read()
#print ("the date is "+ data)


mchaine = "maher"

#if data.__contains__(mchaine) :
if mchaine in  data.lower() :
    data2= data.lower()
    #print ("the date is " + data2)

    print("exist")
else :
    print("not exist ")


#file.write("aaaaaaaaaaaa")

file.close()


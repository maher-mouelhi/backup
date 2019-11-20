filename = "setting.dat"
with open(filename,"wb") as f:
   f.write(b"some string")

with open(filename, "rb") as f_in:
       print("content:  ", f_in.read())

myfile = open(filename,"wb")
user_input = input("enter your name: ")
try:
    myfile.write(user_input.encode('utf8'))
except Exception as e:
    import traceback
    traceback.print_exc()
    raise
    print("not shown")
finally:
    myfile.close()
    print("OK ALL DONE")

with open(filename,"rb") as f_in:
    print(f_in.read().decode('utf8'))

#///reading from text file : mfile
with open("mfile","rb") as f_in:
    print("first carctere:  ",f_in.read(1))
    print("rest of the line:  ",f_in.readline())
    #print(f_in.readlines())

    for line in f_in:
        print("line: ", line)


s= "hello"
print(list(s))

name= "Cristiano Ronaldo"
first,last=name.split()

print("{first}+{last}".format(first=first, last=last))

print("/path/to/a/folder".split("/"))

import os
print(os.environ['PATH'].split(os.pathsep))

print("Apples,Bananas,Chips,Fish".split(","))
print("Apples and Bananas".split("and"))
print("Apples,Bananas,Chips,Fish".split(",",2))

file_path="/some/path/to/somefile.ext"
print(file_path.split("."))
print(file_path.rsplit(".")[0])
print(file_path.rsplit(".")[-1]) # extension
print(file_path.rsplit("/")[-1]) #name file

parts = "Apples and Bananas".split("and")
print(" or ".join(parts))
print(" + ".join(parts))

print(" ".join([str(1),str(2),str(3)])) #cast string


if isinstance(name,str):
    #it is string so we can do treatment
    pass

name.isprintable()
name.isalnum()


print(
    name[0].isdigit(),
    name[0].isspace(),
    name[0].islower(),
    name[0].isupper(),
    name[0].isalpha(),
)


# result = input("Play again ?")

"\r     a string    \n\r\t".strip() == "a string"
"&&a string !!&&".strip("&!") == "a string"
"a string".upper() == "A STRING"
"A StrinG".lower() == "a string"
"A StringG".swapcase() == "a sTRINg"

"yes".startswith("y")
"filename.exe".endswith(".exe")

"a s" in "a string"
print("a string".replace("ring","ar"))


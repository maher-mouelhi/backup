 #qui demande de saisir 2 chaînes de caractères et qui affiche la
#plus grande des 2 chaînes (celle qui a le plus de caractères).


var1 = input("give var1 string ")
var2 = input("give var2 string ")

if len(var1) < len(var2) :
    print(var1)
else: print(var2)
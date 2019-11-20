#input data family 1 and 2

familiesList = []
PersonneDictionary = {"name":'',"age":0}
PersoneList = []


for i in range(2):
    fam = input("data family plz give name ")

    pere = input(" plz give name pere ")
    pereAge = input(" plz give age pere ")

    PersonneDictionary["name"]= pere
    PersonneDictionary["age"]= pereAge
    PersoneList.append(PersonneDictionary)

    mere = input(" plz give name mere ")
    mereAge = input(" plz give age mere ")

    PersonneDictionary["name"] = mere
    PersonneDictionary["age"] = mereAge
    PersoneList.append(PersonneDictionary)
    familiesList.append(PersoneList)






print(familiesList)


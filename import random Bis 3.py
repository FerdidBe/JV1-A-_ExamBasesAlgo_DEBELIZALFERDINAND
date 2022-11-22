myTable = [16,45,9,13,3]
NewVar = myTable[4]
myTable.pop(4)
myTable.insert(0,NewVar)
print (myTable)


myTable = [16,45,9,13,3]
for j in range(len(myTable)):
    
    pluspetit = myTable[j]
    numeropluspetit=j
    for i in range(j,len(myTable)):
        if(pluspetit > myTable[i]):
            pluspetit = myTable[i]
            numeropluspetit = i

    sauvegarde = myTable[j]
    myTable[j] = myTable[numeropluspetit]
    myTable[numeropluspetit] = sauvegarde
print(myTable)

#le tri à bulle est très lent puisqu'il est plus qu'il lit chaque nombre afin de les mettre dans l'ordre. le programme met donc du temps à etre executé, plusieur seconde. 



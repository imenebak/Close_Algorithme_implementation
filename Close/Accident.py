from Close import split as sp


dataBase = {}
def main():
    
    print('DEBUT DE TRAITEMENT')
    maxItemId = sp.readDataFromFileToDataBase(dataBase, "Data/accident_soft.dat")
    print("Les items partent jusqu'au rend : ", maxItemId)

    print("\n\n\n\n\n\nLE SUPP =  ",sp.Supp())
    minSupp = int(sp.MinSup(sp.Supp(),maxItemId))

    print("Valleur MinSup = 2 * Le centre de gravité =  ",minSupp)
    #print("\n\n\n\n\n\nDATA BASE =  ",dataBase)
    postSet = sp.createPostSet(dataBase, maxItemId, minSupp)
    print("\n\n\n Item Fréquent  etape 1 : \n\n",postSet)
    postSet = sp.sortPostSet(postSet, dataBase)

    closedSet = []
    closedSetTIds = []
    preSet = []

    f_out = open("Accidents_out","w")
    sp.dci_closed(True, closedSet, closedSetTIds, postSet, preSet, minSupp, dataBase, f_out)
    f_out.close()



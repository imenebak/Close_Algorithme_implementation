import numpy as np
import matplotlib.pyplot as plt

Supports = {}

#RETURN LE LEN DES ITEMS ET LE SUPPORT DE CHAQUE ITEMSET DE TAILLE 01
def readDataFromFileToDataBase(dataBase, filePath):
    fHandle = open(filePath, "r")
    nTId = 0
    maxItemId = 0
    for i in fHandle.readlines():
        nTId += 1
        lineSplitted = i.split()
        #print(len(lineSplitted))
        
        for value in lineSplitted:
            item = int(value)
            Supports[item] = 0 
            if(item in dataBase):
                dataBase[item] = np.append(dataBase[item], nTId)
            else:
                dataBase[item] = np.array([nTId])
            if(item > maxItemId):
                maxItemId = item
       

    fHandle.close()
    fHandle = open(filePath, "r")
    for i in fHandle.readlines():
        lineSplitted = i.split()
        for value in lineSplitted:
            item = int(value)
            Supports[item] = Supports[item]+1
    fHandle.close()

    #plotData(Supports)
    print(Supports)
    return maxItemId

#PLOTING LES OCCURENCES DES ITEMS
def plotData(Supports):
    lists = sorted(Supports.items()) 
    x, y = zip(*lists) 
    plt.plot(x, y)
    plt.show()

#Calcul du MinSup
def MinSup(vecteur, v):
    MinS = 0
    for i in vecteur.values():
        MinS = MinS+i
    return (MinS/v)*8

#RENVOIE LES SUPPORT INIT        
def Supp():
    return Supports

#ELIMINATION DES ITEMSET NON FREQUENTS
def createPostSet(dataBase, maxItemId, minSuppRelative):
    postSet = []
    #print(dataBase, maxItemId, minSuppRelative)
    for i in range(1, maxItemId + 1):
        try:
            tidSet = dataBase[i]
        except:
            continue
        if(len(tidSet) >= minSuppRelative):
            postSet.append(i)
    return np.array(postSet)

def isSmallerAccordingToSupport(a, b, dataBase):
    sizeA = Supports[a]
    sizeB = Supports[b]
    if(sizeA != sizeB):
        #print("return", sizeA < sizeB)
        return sizeA < sizeB
    else:
        return isSmallerAccordingToOrder(a, b)


def sortPostSet(postSet, dataBase):        
    for i in range(len(postSet)):
        minimum = i       
        for j in range(i + 1, len(postSet)):
            if(isSmallerAccordingToSupport(postSet[minimum], postSet[j], dataBase)):
                minimum = j
        postSet[minimum], postSet[i] = postSet[i], postSet[minimum]
    print(postSet)
    print(np.flip(postSet, 0))
    return np.flip(postSet, 0) 


def isSmallerAccordingToOrder(a, b):
    if(a < b):
        return True
    else:
        return False

def isDup(newGenTIds, preset, dataBase):
    for i in preset:
        if(set(newGenTIds).issubset(set(dataBase[i]))):
            return True   
    return False

def intersectTIdSet(tIdSet1, tIdSet2):
    newTIdSet = []
    if(len(tIdSet1) > len(tIdSet2)):
        for tId in tIdSet2:
            if(np.any(tIdSet1 == tId)):
                newTIdSet.append(tId)
    else:
        for tId in tIdSet1:
            if(np.any(tIdSet2 == tId)):
                newTIdSet.append(tId)
    return np.array(newTIdSet)

def dci_closed(isFirstTime, closedSet, closedSetTIds, postSet, preSet, minSupp, dataBase, f_out):
    for m in range(1, len(postSet)):
        i = postSet[m]
        newGenTIds = []

        if(isFirstTime):
            newGenTIds = dataBase[i]
        else:
            newGenTIds = intersectTIdSet(closedSetTIds, dataBase[i])
        
        if(len(newGenTIds) >= minSupp):
            newGen = np.append(closedSet, np.array([i]))

            if(isDup(newGenTIds, preSet, dataBase) == False):
                closedSetNew = np.array(newGen)

                if(isFirstTime):
                    closedNewTIds = dataBase[i]
                else:
                    closedNewTIds = np.array(newGenTIds)
                
                postSetNew = []

                for j in postSet:

                    if(isSmallerAccordingToSupport(i, j, dataBase)):

                        if(set(newGenTIds).issubset(dataBase[j])):
                            closedSetNew = np.append(closedSetNew, [j])

                            jTIds = dataBase[j]

                            closedNewTIds = intersectTIdSet(closedNewTIds, jTIds)
                        else:
                            postSetNew = np.append(postSetNew, [j])

                # print(numpy.sort(closedSetNew), len(closedNewTIds))
                f_out.write(' '.join(map(repr, closedSetNew.astype(int))) +  " #SUP: " + str(len(closedNewTIds)) + "\n")

                preSetNew = np.array(preSet)
                dci_closed(False, closedSetNew, closedNewTIds, postSetNew, preSetNew,  minSupp, dataBase, f_out)

                preSet = np.append(preSet, [i])

def dci_closed(isFirstTime, closedSet, closedSetTIds, postSet, preSet, minSupp, dataBase, f_out):
    for m in range(1, len(postSet)):
        i = postSet[m]
        newGenTIds = []

        if(isFirstTime):
            newGenTIds = dataBase[i]
        else:
            newGenTIds = intersectTIdSet(closedSetTIds, dataBase[i])
        
        if(len(newGenTIds) >= minSupp):
            newGen = np.append(closedSet, np.array([i]))

            if(isDup(newGenTIds, preSet, dataBase) == False):
                closedSetNew = np.array(newGen)

                if(isFirstTime):
                    closedNewTIds = dataBase[i]
                else:
                    closedNewTIds = np.array(newGenTIds)
                
                postSetNew = []

                for j in postSet:

                    if(isSmallerAccordingToSupport(i, j, dataBase)):

                        if(set(newGenTIds).issubset(dataBase[j])):
                            closedSetNew = np.append(closedSetNew, [j])

                            jTIds = dataBase[j]

                            closedNewTIds = intersectTIdSet(closedNewTIds, jTIds)
                        else:
                            postSetNew = np.append(postSetNew, [j])

                # print(numpy.sort(closedSetNew), len(closedNewTIds))
                f_out.write(' '.join(map(repr, closedSetNew.astype(int))) +  " #SUP: " + str(len(closedNewTIds)) + "\n")

                preSetNew = np.array(preSet)
                dci_closed(False, closedSetNew, closedNewTIds, postSetNew, preSetNew,  minSupp, dataBase, f_out)

                preSet = np.append(preSet, [i])


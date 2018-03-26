from nodeClass import *
import heapq

## This is computePath for Adaptive A*

# setOpen is a binary heap
def ComputePath(listOpen, target, setClose, counter):
    while (target.gVal> listOpen[0][0]):
        temp = listOpen[0][1]
        heapq.heappop(listOpen)
        setClose.append(temp)
        
        if (temp.rNode != temp):
            if (temp.rNode.search < counter) :
                temp.rNode.gVal = float('Inf')
                temp.rNode.search = counter
            if (temp.rNode.gVal > temp.gVal + 1) :
                temp.rNode.gVal = temp.gVal +1
                temp.rNode.tree = temp
                ifRemove = 0
                for key in listOpen:
                    if key[1]==temp.rNode:
                        listOpen.remove(key)
                        ifRemove = 1
                        break
                f = temp.rNode.gVal + temp.rNode.h_fun(temp.rNode,target)
                if ifRemove ==1:
                    listOpen.append([f,temp.rNode])
                    heapq.heapify(listOpen)
                else:
                    heapq.heappush(listOpen,[f,temp.rNode])
                    
        if (temp.lNode != temp):
            if (temp.lNode.search < counter) :
                temp.lNode.gVal = float('Inf')
                temp.lNode.search = counter
            if (temp.lNode.gVal > temp.gVal + 1) :
                temp.lNode.gVal = temp.gVal +1
                temp.lNode.tree = temp
                ifRemove = 0
                for key in listOpen:
                    if key[1]==temp.lNode:
                        listOpen.remove(key)
                        ifRemove = 1
                        break
                f = temp.lNode.gVal + temp.lNode.h_fun(temp.lNode,target)
                if ifRemove ==1:
                    listOpen.append([f,temp.lNode])
                    heapq.heapify(listOpen)
                else:
                    heapq.heappush(listOpen,[f,temp.lNode])

        if (temp.uNode != temp):
            if (temp.uNode.search < counter) :
                temp.uNode.gVal = float('Inf')
                temp.uNode.search = counter
            if (temp.uNode.gVal > temp.gVal + 1) :
                temp.uNode.gVal = temp.gVal +1
                temp.uNode.tree = temp
                ifRemove = 0
                for key in listOpen:
                    if key[1]==temp.uNode:
                        listOpen.remove(key)
                        ifRemove = 1
                        break
                f = temp.uNode.gVal + temp.uNode.h_fun(temp.uNode,target)
                if ifRemove ==1:
                    listOpen.append([f,temp.uNode])
                    heapq.heapify(listOpen)
                else:
                    heapq.heappush(listOpen,[f,temp.uNode])
                    
        if (temp.dNode != temp):
            if (temp.dNode.search < counter) :
                temp.dNode.gVal = float('Inf')
                temp.dNode.search = counter
            if (temp.dNode.gVal > temp.gVal + 1) :
                temp.dNode.gVal = temp.gVal +1
                temp.dNode.tree = temp
                ifRemove = 0
                for key in listOpen:
                    if key[1]==temp.dNode:
                        listOpen.remove(key)
                        ifRemove = 1
                        break
                f = temp.dNode.gVal + temp.dNode.h_fun(temp.dNode,target)
                if ifRemove ==1:
                    listOpen.append([f,temp.dNode])
                    heapq.heapify(listOpen)
                else:
                    heapq.heappush(listOpen,[f,temp.dNode])
#        print(len(listOpen))
        if len(listOpen) == 0:
            return
        
    print(setClose)
    for i in range (0,len(setClose)):
        setClose[i].hVal = target.gVal - setClose[i].gVal




from nodeClass import *
from random import*
import pickle
import sys

sys.setrecursionlimit(10000)

row = 50
col = 50
world = []
for i in range(row):
    layer = []
    for j in range(col):
        temp = Node()
        temp.cor = [i,j]
        ran = uniform(0,1)
        if (ran>0.7):
            temp.block = 1
        else:
            temp.block = 0
            if (i!=0 and world[i-1][j].block == 0):
                temp.uNode = world[i-1][j]
                world[i-1][j].dNode = temp
            if (j!=0 and layer[j-1].block == 0):
                temp.lNode = layer[j-1]
                layer[j-1].rNode = temp
##        print(temp.block,end='')
        layer.append(temp)
##    print('')
    world.append(layer)


blankworld = []
for i in range(row):
    layer = []
    for j in range(col):
        temp = Node()
        temp.cor = [i,j]
        temp.block = 0
        if i!=0:
            temp.uNode = blankworld[i-1][j]
            blankworld[i-1][j].dNode = temp
        if j!=0:
            temp.lNode = layer[j-1]
            layer[j-1].rNode = temp
##        print(temp.block,end='')
        layer.append(temp)
##    print('')
    blankworld.append(layer)
    
f = open("Blankworld.dat","wb")
pickle.dump(blankworld,f)
f.close()

f = open("Gridworld.dat","wb")
pickle.dump(world,f)
f.close()

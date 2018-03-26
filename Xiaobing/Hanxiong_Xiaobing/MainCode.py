import pickle
import heapq
import time
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pylab as plt
from ComputePath import *
from nodeClass import *
from updateMap import *

world = pickle.load(open("Gridworld.dat",'rb'))
blankworld = pickle.load(open("Blankworld.dat",'rb'))

rownum = colnum = len(blankworld)

## Indicator of forward or backward, default 0 is forward.
flag = 0
##for key1 in world:
##    for key2 in key1:
##        print(key2.block,end='')
##    print('')
## measure the total expanded cells
total = 0

counter = 0
priority = 0
## default the start point and the goal point
start = blankworld[0][0]
goal = blankworld[30][48]

start_time = time.time()

while (start != goal):
    if world[start.cor[0]][start.cor[1]].block==1 or world[goal.cor[0]][goal.cor[1]].block==1 :
        print("Invalid input")
        break
    counter = counter + 1
    if flag == 1:
        temp = goal
        goal = start
        start = temp
    start.gVal = 0
    start.search = counter
    goal.gVal = float('Inf')
    goal.search = counter
    listOpen =[]
    f = start.h_fun(start,goal) + start.gVal
##    add start.gVal
##    larger g value
    priority = 100*f - start.gVal
##    smaller g value
##    priority = 100*f + start.gVal
    
##    stardard one, without priority for g value
##    heapq.heappush(listOpen,[f,start])
    heapq.heappush(listOpen,[f,start,priority])
    setClose = []
    ComputePath(listOpen, goal, setClose, counter, total)
    total = total + len(setClose) 
    if len(listOpen) ==0:
        print("I cannot reach the target.")
        break
    else:

## Forward only, disable this part if running backward
        if flag == 0:
            currNode = goal
            prevNode = goal
            while (currNode!= start):
                nextNode = currNode.tree
                currNode.tree = prevNode
                prevNode = currNode
                currNode = nextNode
            start.tree = prevNode
## Forward and Backward shared part
        if flag == 1:
            temp2 = goal
            goal = start
            start = temp2
        head = start ## here head is start.        
        while (head != goal):
            head.block = 2
            updateMap(head,world,blankworld)
            if world[head.tree.cor[0]][head.tree.cor[1]].block != 1:
                head = head.tree
            else:
                break
        start = head
        if start == goal:
            goal.block = 5
##        print("time step ",counter)
##        
## print discovered world       
##        for key1 in blankworld:
##            for key2 in key1:
##                print(key2.block,end='')
##            print('')
##        print('')
if (start == goal and start.block!=1):
    print("I reached the taregt")
elapsed_time = time.time() - start_time
print(elapsed_time)
blankworld[0][0].block = 3

M=np.zeros((rownum,colnum))
i = 0
for key1 in blankworld:
    j = 0
    for key2 in key1:
        M[i,j] = key2.block
        j = j + 1
    i = i + 1
    
##plt.imshow(M, interpolation='nearest', cmap=plt.cm.ocean)
plt.imshow(M)
patch = mpatches.Patch(color='yellow',label='is Goal')
plt.legend(handles=[patch])
plt.colorbar()
plt.show()

## below codes are used to generate the actual maze
##M2=np.zeros((rownum,colnum))
##
##i2 = 0
##for key1 in world:
##    j2 = 0
##    for key2 in key1:
##        M2[i2,j2] = key2.block
##        j2 = j2 + 1
##    i2 = i2 + 1
## show actual maze or not
##plt.imshow(M2)
##patch = mpatches.Patch(color='yellow',label='is Blocked')
##plt.legend(handles=[patch])
##plt.colorbar()
##plt.show()

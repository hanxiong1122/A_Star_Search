import pickle
import heapq
from ComputePath import *
from nodeClass import *
from updateMap import *

world = pickle.load(open("Gridworld.dat",'rb'))
blankworld = pickle.load(open("Blankworld.dat",'rb'))

for key1 in world:
    for key2 in key1:
        print(key2.block,end='')
    print('')

counter = 0

start = blankworld[1][0]
goal = blankworld[6][9]


while (start != goal):
    if world[start.cor[0]][start.cor[1]].block==1 or world[goal.cor[0]][goal.cor[1]].block==1 :
        print("Invalid input")
        break
    counter = counter + 1
    goal.gVal = 0
    start.search = counter
    start.gVal = float('Inf')
    start.search = counter
    listOpen =[]
    f = goal.h_fun(start,goal) + goal.gVal
    heapq.heappush(listOpen,[f,goal])
    setClose = []
    ComputePath(listOpen, start, setClose, counter)
    if len(listOpen) ==0:
        print("I cannot reach the target.")
        break
    else:

## backward
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
            goal.block = 9  
        print("time step ",counter)
        
## print discovered world       
        for key1 in blankworld:
            for key2 in key1:
                print(key2.block,end='')
            print('')
        print('')
if (start == goal and start.block!=1):
    print("I reached the taregt")
   

    

    
    

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

start = blankworld[0][0]
goal = blankworld[2][4]

while (start != goal):
    if world[start.cor[0]][start.cor[1]].block==1 or world[goal.cor[0]][goal.cor[1]].block==1 :
        print("Invalid input")
        break
    counter = counter + 1
    start.gVal = 0
    start.search = counter
    goal.gVal = float('Inf')
    goal.search = counter
    listOpen =[]
    setClose = []
    f = start.h_fun(start,goal) + start.gVal
    heapq.heappush(listOpen,[f,start])

    ComputePath(listOpen, goal, setClose, counter)
    if len(listOpen) ==0:
        print("I cannot reach the target.")
        break
    else:
        currNode = goal
        prevNode = goal
        while (currNode!= start):
            nextNode = currNode.tree
            currNode.tree = prevNode
            prevNode = currNode
            currNode = nextNode
        start.tree = prevNode
        head = start ## here head is start        
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
        for key1 in blankworld:
            for key2 in key1:
                print(key2.block,end='')
            print('')
        print('')
if (start == goal and start.block!=1):
    print("I reached the taregt")
   

    

    
    

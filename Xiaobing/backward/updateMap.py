from nodeClass import *
def updateMap(cell,world,blankworld):
	x = cell.cor[0]
	y = cell.cor[1]


	if (x>0 and world[x-1][y].block==1):
		blankworld[x-1][y].block = 1
		blankworld[x][y].uNode = blankworld[x][y]
		blankworld[x-1][y].dNode = blankworld[x-1][y]

	if (x<=len(blankworld)-2 and world[x+1][y].block==1):
		blankworld[x+1][y].block = 1
		blankworld[x][y].dNode = blankworld[x][y]
		blankworld[x+1][y].uNode = blankworld[x+1][y]

	if (y>0 and world[x][y-1].block==1):
		blankworld[x][y-1].block = 1
		blankworld[x][y].lNode = blankworld[x][y]
		blankworld[x][y-1].rNode = blankworld[x][y-1]

	if (y<=len(blankworld[0])-2 and world[x][y+1].block==1):
		blankworld[x][y+1].block = 1
		blankworld[x][y].rNode = blankworld[x][y]
		blankworld[x][y+1].lNode = blankworld[x][y+1]


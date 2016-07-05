import scipy
import networkx

#           0         1          2        3          4         5      6        7       8           9               10            11                12             13              14               15              16           17
names = ["Gromp","Blue Buff","Wolves","Wraiths","Red Buff","Golems","Tri","Baron","Dragon","Lower Scuttle","Upper Scuttle","Enemy Gromp","Enemy Blue Buff","Enemy Wolves","Enemy Wraiths","Enemy Red Buff","Enemy Golems","Enemy Tri",       "Top","Mid","Bot","Base"]
#     18    19    20     21

graph = networkx.DiGraph()
for i in range(len(names)):
	graph.add_node(i,name=names[i])

graph[0][10]["weight"] = 0.15 #gromp to scuttle
graph[0][1]["weight"] = 0.5 #gromp to blue
graph[0][2]["weight"] = 0.2 #gromp to wolves
graph[0][18]["weight"] = 0.15 #gromp to top

graph[1][0]["weight"] = 0.15 #blue to gromp
graph[1][2]["weight"] = 0.15 #blue to wolves
graph[1][10]["weight"] = 0.2#blue to scuttle
graph[1][18]["weight"] = 0.2#blue to top
graph[1][19]["weight"] = 0.3#blue to mid

graph[2][0]["weight"] = 0.2 #wolves to gromp
graph[2][1]["weight"] = 0.4 #wolves to blue
graph[2][19]["weight"] = 0.4 #wolves to mid

graph[3][19]["weight"] = 0.3 #wraiths to mid
graph[3][4]["weight"] = 0.4 #wraiths to red
graph[3][9]["weight"] = 0.3 #wraiths to scuttle

graph[4][3]["weight"] = 0.1 #red to wraiths
graph[4][5]["weight"] = 0.1 #red to golems
graph[4][9]["weight"] = 0.2 #red to scuttle
graph[4][20]["weight"] = 0.2 #red to bot
graph[4][19]["weight"] = 0.3 #red to mid
graph[4][6]["weight"] = 0.1 #red to tri

graph[5][9]["weight"] = 0.2 #golems to scuttle
graph[5][4]["weight"] = 0.4 #golems to red
graph[5][20]["weight"] = 0.3 #golems to bot
graph[5][6]["weight"] = 0.1 #golems to tri

graph[6][4]["weight"] = 0.25 #tri to red
graph[6][5]["weight"] = 0.25 #tri to golems
graph[6][20]["weight"] = 0.5 #tri to bot

graph[7][10]["weight"] = 0.9 #baron to scuttle
graph[7][15]["weight"] = 0.1 #baron to enemy red

graph[8][9]["weight"] = 0.9 #dragon to scuttle
graph[8][4]["weight"] = 0.1 #dragon to red

graph[9][12]["weight"] = 0.2 #bot scuttle to enemy blue
graph[9][20]["weight"] = 0.2 #bot scuttle to bot
graph[9][6]["weight"] = 0.1 #bot scuttle to tri
graph[9][3]["weight"] = 0.2 #bot scuttle to wraiths
graph[9][19]["weight"] = 0.2 #bot scuttle to mid
graph[9][8]["weight"] = 0.1 #bot scuttle to dragon

graph[10][8]["weight"] = 0.2 #top scuttle to blue
graph[10][8]["weight"] = 0.2 #top scuttle to mid
graph[10][8]["weight"] = 0.2 #top scuttle to enemy wraiths
graph[10][8]["weight"] = 0.1 #top scuttle to enemy tri
graph[10][8]["weight"] = 0.2 #top scuttle to top
graph[10][8]["weight"] = 0.1 #top scuttle to baron

graph[11][9]["weight"] = 0.15 #gromp to scuttle
graph[11][13]["weight"] = 0.5 #gromp to blue
graph[11][12]["weight"] = 0.2 #gromp to wolves
graph[11][20]["weight"] = 0.15 #gromp to bot

graph[12][11]["weight"] = 0.15 #blue to gromp
graph[12][13]["weight"] = 0.15 #blue to wolves
graph[12][9]["weight"] = 0.2#blue to scuttle
graph[12][20]["weight"] = 0.2#blue to bot
graph[12][19]["weight"] = 0.3#blue to mid

graph[13][11]["weight"] = 0.2 #wolves to gromp
graph[13][12]["weight"] = 0.4 #wolves to blue
graph[13][19]["weight"] = 0.4 #wolves to mid

graph[14][19]["weight"] = 0.3 #wraiths to mid
graph[14][15]["weight"] = 0.4 #wraiths to red
graph[14][8]["weight"] = 0.3 #wraiths to scuttle

graph[15][14]["weight"] = 0.1 #red to wraiths
graph[15][16]["weight"] = 0.1 #red to golems
graph[15][8]["weight"] = 0.2 #red to scuttle
graph[15][18]["weight"] = 0.2 #red to top
graph[15][19]["weight"] = 0.3 #red to mid
graph[15][17]["weight"] = 0.1 #red to tri

graph[16][8]["weight"] = 0.2 #golems to scuttle
graph[16][15]["weight"] = 0.4 #golems to red
graph[16][18]["weight"] = 0.3 #golems to top
graph[16][17]["weight"] = 0.1 #golems to tri

graph[17][15]["weight"] = 0.25 #tri to red
graph[17][16]["weight"] = 0.25 #tri to golems
graph[17][18]["weight"] = 0.5 #tri to top

graph[18][10]["weight"] = 0.5 #top to tri
graph[18][10]["weight"] = 0.5 #top to scuttle

graph[19][9]["weight"] = 0.2 #mid to bot scuttle
graph[19][10]["weight"] = 0.2 #mid to top scuttle
graph[19][14]["weight"] = 0.1 #mid to wraiths
graph[19][3]["weight"] = 0.1 #mid to wraiths
graph[19][1]["weight"] = 0.1 #mid to blue
graph[19][2]["weight"] = 0.1 #mid to wolves
graph[19][12]["weight"] = 0.1 #mid to blue
graph[19][13]["weight"] = 0.1 #mid to wolves

graph[20][9]["weight"] = 0.5 #bot to scuttle
graph[20][6]["weight"] = 0.5 #bot to tri

graph[21][6]["weight"] = 0.1 #base to top
graph[21][6]["weight"] = 0.1 #base to mid
graph[21][6]["weight"] = 0.1 #base to bot
graph[21][6]["weight"] = 0.1 #base to wraiths
graph[21][6]["weight"] = 0.1 #base to red
graph[21][6]["weight"] = 0.1 #base to golems
graph[21][6]["weight"] = 0.1 #base to blue
graph[21][6]["weight"] = 0.1 #base to wolves
graph[21][6]["weight"] = 0.1 #base to gromp
graph[21][6]["weight"] = 0.05 #base to baron
graph[21][6]["weight"] = 0.05 #base to dragon

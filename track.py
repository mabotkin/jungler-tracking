import numpy.linalg

#           0         1          2        3          4         5      6        7       8           9               10            11                12             13              14               15              16           17
names = ["Gromp","Blue Buff","Wolves","Wraiths","Red Buff","Golems","Tri","Baron","Dragon","Lower Scuttle","Upper Scuttle","Enemy Gromp","Enemy Blue Buff","Enemy Wolves","Enemy Wraiths","Enemy Red Buff","Enemy Golems","Enemy Tri",       "Top","Mid","Bot","Base"]
#     18    19    20     21
graph = [[0 for i in range(len(names))] for i in range(len(names))]

graph[0][10] = 0.1 #gromp to scuttle
graph[0][1] = 0.4 #gromp to blue
graph[0][2] = 0.2 #gromp to wolves
graph[0][18] = 0.1 #gromp to top
graph[0][21] = 0.1 #gromp to base
graph[0][0] = 0.1 #self

graph[1][0] = 0.1 #blue to gromp
graph[1][2] = 0.1 #blue to wolves
graph[1][10] = 0.2 #blue to scuttle
graph[1][18] = 0.2 #blue to top
graph[1][19] = 0.2 #blue to mid
graph[1][21] = 0.1 #blue to base
graph[1][1] = 0.1 #self

graph[2][0] = 0.2 #wolves to gromp
graph[2][1] = 0.3 #wolves to blue
graph[2][19] = 0.3 #wolves to mid
graph[2][21] = 0.1 #wolves to base
graph[2][2] = 0.1 #self

graph[3][19] = 0.25 #wraiths to mid
graph[3][4] = 0.3 #wraiths to red
graph[3][9] = 0.25 #wraiths to scuttle
graph[3][21] = 0.1 #wraiths to base
graph[3][3] = 0.1 #self

graph[4][3] = 0.1 #red to wraiths
graph[4][5] = 0.1 #red to golems
graph[4][9] = 0.2 #red to scuttle
graph[4][20] = 0.15 #red to bot
graph[4][19] = 0.15 #red to mid
graph[4][6] = 0.1 #red to tri
graph[4][21] = 0.1 #red to base
graph[4][4] = 0.1 #self

graph[5][9] = 0.2 #golems to scuttle
graph[5][4] = 0.25 #golems to red
graph[5][20] = 0.25 #golems to bot
graph[5][6] = 0.1 #golems to tri
graph[5][21] = 0.1 #golems to base
graph[5][5] = 0.1 #self

graph[6][4] = 0.2 #tri to red
graph[6][5] = 0.2 #tri to golems
graph[6][20] = 0.5 #tri to bot
graph[6][21] = 0.1 #tri to base

graph[7][10] = 0.7 #baron to scuttle
graph[7][15] = 0.1 #baron to enemy red
graph[7][21] = 0.1 #baron to base
graph[7][7] = 0.1 #self

graph[8][9] = 0.7 #dragon to scuttle
graph[8][4] = 0.1 #dragon to red
graph[8][21] = 0.1 #dragon to base
graph[8][8] = 0.1 #self

graph[9][12] = 0.2 #bot scuttle to enemy blue
graph[9][20] = 0.2 #bot scuttle to bot
graph[9][6] = 0.1 #bot scuttle to tri
graph[9][3] = 0.05 #bot scuttle to wraiths
graph[9][19] = 0.2 #bot scuttle to mid
graph[9][8] = 0.05 #bot scuttle to dragon
graph[9][21] = 0.1 #bot scuttle to base
graph[9][9] = 0.1 #self

graph[10][1] = 0.05 #top scuttle to blue
graph[10][19] = 0.2 #top scuttle to mid
graph[10][14] = 0.2 #top scuttle to enemy wraiths
graph[10][17] = 0.1 #top scuttle to enemy tri
graph[10][18] = 0.2 #top scuttle to top
graph[10][7] = 0.05 #top scuttle to baron
graph[10][21] = 0.1 #top scuttle to base
graph[10][10] = 0.1 #self

graph[11][9] = 0.1 #gromp to scuttle
graph[11][13] = 0.4 #gromp to blue
graph[11][12] = 0.2 #gromp to wolves
graph[11][20] = 0.1 #gromp to bot
graph[11][21] = 0.1 #gromp to base
graph[11][11] = 0.1 #self

graph[12][11] = 0.1 #blue to gromp
graph[12][13] = 0.1 #blue to wolves
graph[12][9] = 0.2 #blue to scuttle
graph[12][20] = 0.2 #blue to bot
graph[12][19] = 0.2 #blue to mid
graph[12][21] = 0.1 #blue to base
graph[12][12] = 0.1 #self

graph[13][11] = 0.2 #wolves to gromp
graph[13][12] = 0.3 #wolves to blue
graph[13][19] = 0.3 #wolves to mid
graph[13][21] = 0.1 #wolves to base
graph[13][13] = 0.1 #self

graph[14][19] = 0.25 #wraiths to mid
graph[14][15] = 0.3 #wraiths to red
graph[14][8] = 0.25 #wraiths to scuttle
graph[14][21] = 0.1 #wraiths to base
graph[14][14] = 0.1 #self

graph[15][14] = 0.1 #red to wraiths
graph[15][16] = 0.1 #red to golems
graph[15][8] = 0.2 #red to scuttle
graph[15][18] = 0.15 #red to top
graph[15][19] = 0.15 #red to mid
graph[15][17] = 0.1 #red to tri
graph[15][21] = 0.1 #red to base
graph[15][15] = 0.1 #self

graph[16][8] = 0.2 #golems to scuttle
graph[16][15] = 0.25 #golems to red
graph[16][18] = 0.25 #golems to top
graph[16][17] = 0.1 #golems to tri
graph[16][21] = 0.1 #golems to base
graph[16][16] = 0.1 #self

graph[17][15] = 0.2 #tri to red
graph[17][16] = 0.2 #tri to golems
graph[17][18] = 0.5 #tri to top
graph[17][21] = 0.1 #tri to base

graph[18][17] = 0.45 #top to tri
graph[18][10] = 0.45 #top to scuttle
graph[18][21] = 0.1 #top to base

graph[19][9] = 0.2 #mid to bot scuttle
graph[19][10] = 0.2 #mid to top scuttle
graph[19][14] = 0.1 #mid to wraiths
graph[19][3] = 0.1 #mid to wraiths
graph[19][1] = 0.1 #mid to blue
graph[19][2] = 0.05 #mid to wolves
graph[19][12] = 0.1 #mid to blue
graph[19][13] = 0.05 #mid to wolves
graph[19][21] = 0.1 #mid to base

graph[20][9] = 0.45 #bot to scuttle
graph[20][6] = 0.45 #bot to tri
graph[20][21] = 0.1 #bot to base

graph[21][18] = 0.1 #base to top
graph[21][19] = 0.1 #base to mid
graph[21][20] = 0.1 #base to bot
graph[21][14] = 0.1 #base to wraiths
graph[21][15] = 0.1 #base to red
graph[21][16] = 0.1 #base to golems
graph[21][12] = 0.1 #base to blue
graph[21][13] = 0.1 #base to wolves
graph[21][11] = 0.1 #base to gromp
graph[21][7] = 0.05 #base to baron
graph[21][8] = 0.05 #base to dragon

A = numpy.array(graph)
A = A.transpose()

#for i in range(len(A)):
#	tot = 0
#	for j in range(len(A[0])):
#		tot += A[j][i]
#	print i, tot

#print A
#print numpy.linalg.eigvals(A)
x,v = numpy.linalg.eig(A)
#print v
#x = (numpy.linalg.eig(A)[0][1:])
#print x
#print v
#print x[0]
tot = 0
for i in range(len(v[:,0])):
	tot += numpy.real(v[:,0][i])
	
x = []
for i in range(len(names)):
	if i != 1:
		x.append(0)
	else:
		x.append(1)
x = numpy.array(x).transpose()

for k in range(5):
	print "Iteration " + str(k) + ":"
	print "------------"
	for i in range(len(v[:,0])):
		print names[i] + " " + str(x[i])	
	print "------------"
	x = A.dot(x)

print "EIGENVECTOR:"
print "------------"
for i in range(len(v[:,0])):
	print names[i] + " " + str(float(numpy.real(v[:,0][i]/float(tot))))
print "------------"

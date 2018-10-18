import numpy as npgi

universe = np.zeros((6,6))

beacon = [
[1,1,0,0],
[1,1,0,0],
[0,0,1,1],
[0,0,1,1]
]


universe[1:5, 1:5] = beacon
print(universe) 	
def count_neighbours(u,x,y):
	neighbours = 0
	for ix,row in enumerate(u):
		for iy,elm in enumerate(row):
			if(u[ix][iy] == 1.0):
				neighbours = neighbours + 1
	return neighbours-1

def check_health(u,r,c,num_neighbours):
	if(not 2 <= num_neighbours <= 3):
		# u[r][c] = 0.0
		return 0
	elif(num_neighbours == 3):
		#u[r][c] = 1.0
		return 1
		
def life_proccessing(u):
	for irow,row in enumerate(u):
		for icol ,col in enumerate(row):
			if(u[irow][icol] == 1.0):
				u1= u[irow-1:irow+2,icol-1:icol+2]
				print(u1)
				neighbours = count_neighbours(u1,irow,icol)
				print(neighbours)
				cell_status = check_health(u1,irow,icol,neighbours)
				print(cell_status)
				print("row " +str(irow)+" col : "+ str(icol)
				if(cell_status == 0):
					u[irow][icol]=0.0
				new_u = u
	return new_u
print("###########################")
print(life_proccessing(universe))


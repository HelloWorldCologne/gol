import numpy as np
import copy
universe = np.zeros((6,6))

beacon = [
[1,1,0,0],
[1,1,0,0],
[0,0,1,1],
[0,0,1,1]
]


universe[1:5, 1:5] = beacon
print(universe)

def life_proccessing(u):
	new_u = u.copy()
	for irow,row in enumerate(u):
		for icol ,elm in enumerate(row):
			num_neighbours = count_neighbours(u,irow,icol)
			new_u[irow][icol] = check_health(elm,num_neighbours)
	return new_u

def count_neighbours(u,ir,ic):
	u1= u[ir-1:ir+2,ic-1:ic+2]
	return count_ones(u1)-u[ir][ic]

def count_ones(u):
	neighbours = 0
	for ir,row in enumerate(u):
		for ic,elm in enumerate(row):
			if(elm == 1.0):
				neighbours = neighbours + 1
	return neighbours

def check_health(elm,num_neighbours):
	if(elm == 1):
		return check_health_live_cell(num_neighbours)
	else:
		return check_health_dead_cell(num_neighbours)

def check_health_live_cell(num_neighbours):
	if(num_neighbours < 2 or num_neighbours > 3):
		return 0
	else:
		return 1
def check_health_dead_cell(num_neighbours):
	if(num_neighbours == 3):
		return 1
	else:
		return 0

print("###########################")
print(life_proccessing(universe))


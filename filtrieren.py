import numpy as np
import random

terrain = np.matrix(
[['H', 'N', 'T'],
['N', 'N', 'N'],
['N', 'B', 'H']])

prior = np.matrix(
[[0.125, 0.125, 0.125],
[0.125, 0.125, 0.125], 
[0.125, 0, 0.125]]) #prior[2,1] == 'B'

given_actions = ['R', 'R', 'D', 'D']
given_readings = ['N', 'N', 'H', 'H']

def TransitionModel(mappo, cellfromimmutable, action):
	cellfrom = list(cellfromimmutable)
	cellto = cellfrom #cellto changes when cellfrom changes. bc python
	if action == 'R':
		cellto[0] += 1
	elif action == 'L':
		cellto[0] -= 1
	elif action == 'U':
		cellto[1] += 1
	elif action == 'D':
		cellto[1] -= 1
	else:
		return nil

	if cellto[0] <= -1 or cellto[1] <= -1:
		return list(cellfromimmutable)
	elif cellto[0] >= np.shape(mappo)[0] or cellto[1] >= np.shape(mappo)[1]:
		return list(cellfromimmutable)
	elif (mappo[tuple(cellto)] == 'B'):
		return list(cellfromimmutable)

	if random.randrange(0, 100) < 90:
		return cellto
	else:
		return list(cellfromimmutable) 

def ObservationModel(reading):
	prob = random.randrange(0, 100)
	if prob < 90:
		return reading
	elif prob >= 90 and prob < 95:
		if reading == 'N':
			return 'H'
		elif reading == 'H':
			return 'T'
		elif reading == 'T':
			return 'N'
	elif prob >= 95 and prob < 100:
		if reading == 'N':
			return 'T'
		elif reading == 'H':
			return 'N'
		elif reading == 'T':
			return 'H'
			
def Filter(mappo, action, reading):

	for x in range(0, np.shape(mappo)[0]):
		for y in range(0, np.shape(mappo)[1]):
			priorbelief = mappo[(x,y)]
			#multiply priorbelief by TM and OM

	#for stateprob in np.nditer(mappo):
	#	print stateprob

	return mappo

def main():
	map1 = Filter(prior, given_actions[0], given_readings[0])
	#map2 = Filter(map1, given_actions[1], given_readings[1])
	#map3 = Filter(map2, given_actions[2], given_readings[2])
	#map4 = Filter(map3, given_actions[3], given_readings[3])

	print map1

#print TransitionModel((2,0), 'Right') #cannot do so, other is blocked
#print ObservationModel(terrain[2,0])

if __name__ == "__main__":
	main()


class trails:

	# initialize a 3D matrix with all the feasible moves 
	def __init__():

		s.trails = dict()

	def update(s, x, y, z)
		""" update trails used by ant """

		# TODO that will be a critical section 

		if not s.trails.has_key(x):
			s.trails[x] = dict()

		if not s.trails[x].has_key(y):
			s.trails[x][y] = dict()

		if not s.trails[x][y].has_key(z):
			s.trails[x][y][z] = 0

		s.trails[x][y][z] = s.trails[x][y][z] + 1

		# end of critical section


	def value(s, x, y, z)
		""" return trails value of a path """

		# TODO critical section
		if s.trails.has_key(x) and s.trails[x].has_ke(y) and s.trails[x][y].has_key(z):
			return s.trails[x][y][z]
		# end critical section 

		return 0

	def evaporate(s):
		# TODO 

	

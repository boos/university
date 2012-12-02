import thread

class trails:

	# initialize a 3D matrix with all the feasible moves 
	def __init__(s):

		s.trails = dict()
		s.lock = thread.allocate_lock()

	def update(s, selected_move):
		""" update trails used by ant """

		x = selected_move[0]
		y = selected_move[1]
		z = selected_move[2]

		# start of critical section 
		s.lock.acquire()

		if not s.trails.has_key(x):
			s.trails[x] = dict()

		if not s.trails[x].has_key(y):
			s.trails[x][y] = dict()

		if not s.trails[x][y].has_key(z):
			s.trails[x][y][z] = 0

		s.trails[x][y][z] = s.trails[x][y][z] + 1

		s.lock.release()
		# end of critical section


	def value(s, x, y, z):
		""" return trails value of a path """

		value = 0 

		s.lock.acquire()

		# start of critical section 
		if s.trails.has_key(x) and s.trails[x].has_ke(y) and s.trails[x][y].has_key(z):
			value = s.trails[x][y][z]

		s.lock.release()
		# end of critical secion 

		return value

	def evaporate(s):
		# TODO 
		# did I need this functionality ?


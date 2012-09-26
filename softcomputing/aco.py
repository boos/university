import random

class ANT:
	""" ANT class. """

	# restrict the min and max available move range
	MIN_MOVE = 0.0001
	MAX_MOVE = 10.000

	# tabu set of all unfeasible move 
	tabu = set()
	
	def feasible_moves(self):
		""" compute a set of feasible moves """
		pass

	def chose_move(self):
		""" statistically select wich of the feasible move is the right one to select """
		pass

	def move(self):
		""" compute the move and record it in the current solution """
		pass




class ACO:
	""" ANT COLONY OPTIMIZATION PYTHON IMPLEMENTATION """

	def __init__(self):
		pass

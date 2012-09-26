import random


class ANT:
	""" ANT class. """

	# restrict the min and max available move range
	MIN_RANGE = -10
	MAX_RANGE = +10

	AVAILABLE_MOVES = 

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

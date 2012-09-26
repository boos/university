import numpy as np
import random

# TODO
#
# NEED_TO_HAVE:
# 	- ALL available MOVES pre computed
#

# NEET_TO_DO:
# 	- SELECT a subset of all available moves 
#	- COMPUTE which one are more proficient to be selected
#	- 

class ANT:
	""" ANT class. """

	# available rotation moves from 0 to 360 
	# available translation moves from -10.0 to +10.0 with 0.1 steps
	AVAILABLE_ROTATION_MOVES = np.arange(0,360)
	AVAILABLE_TRASLATION_MOVES = np.arange(-10,+10.1,0.1)

	# list that contains temporary feasible moves
	FEASIBLE_MOVES_SIZE = 30
	feasible_moves = list()

	# list with all the selected computed moves
	selected_moves = list() 

	def __init__(self):
		""" Initialize the first step of the  partial solution """
		self.selected_moves.append(self.compute_a_move())

	def compute_a_move(self):
		""" This function returns errror correction in roto-traslation.
			
			Values are in RX,RY,RZ on rotation.
			Values are in TX,TY,TZ in traslation."""

		# chose randomly move
		RX = self.AVAILABLE_ROTATION_MOVES[random.randrange(0,360)]
		RY = self.AVAILABLE_ROTATION_MOVES[random.randrange(0,360)]
		RZ = self.AVAILABLE_ROTATION_MOVES[random.randrange(0,360)]

		TX = self.AVAILABLE_TRASLATION_MOVES[random.randrange(0,201)]
		TY = self.AVAILABLE_TRASLATION_MOVES[random.randrange(0,201)]
		TZ = self.AVAILABLE_TRASLATION_MOVES[random.randrange(0,201)]

		return np.array([RX,RY,RZ,TX,TY,TZ])

	def feasible_moves_creation(self):
		""" compute a set of feasible moves """
		for available_moves in range(1, self.FEASIBLE_MOVES_SIZE):
			self.feasible_moves.append(self.compute_a_move())

		return self.feasible_moves

	def feasible_moves_selection(self):
		""" statistically select wich of the feasible move is the right one to select """
		return self.feasible_moves[1]

	def move(self):
		""" compute a set of feasible moves, chose one of that and add it in the current solution """
		self.feasible_moves_creation()
		self.selected_moves.append(self.feasible_moves_selection())

def testunit():
	atomic_ant = ANT()
	atomic_ant.feasible_moves_creation()
	atomic_ant.feasible_moves_selection()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()

	print atomic_ant.selected_moves

__init__ = testunit()

import numpy as np
import random

import geometric_trasformation

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


	def __init__(self, real_position, trails, attr_weight, trails_weight):
		""" Initialize the first step of the  partial solution 
        
            Set also the coefficient weight of trail with respect to attractivness """

		# store locally where the real position is 
		self.real_position = real_position

		# store locally attr_weight and trail_weight 
        self.attractiveness_weight = attr_weight
        self.trails_weight = trails_weight

		# all ANT will start to explore solution from the origin
		self.selected_moves.append(np.array[[0],[0],[0]])

		# store locally the reference to the trails 
		self.trails = trails

	def compute_fitness(self, evaluated_position):
		""" compute the distance beetween evaluated_position and actual_position"""

		X = np.absolute(evaluated_position[0] - self.actual_position[0])
		Y = np.absolute(evaluated_position[0] - self.actual_position[0])
		Z = np.absolute(evaluated_position[0] - self.actual_position[0])

		return X + Y + Z


	def compute_a_move(self):
		""" This function returns errror correction in roto-traslation.
			
			Values are in RX,RY,RZ on rotation.
			Values are in TX,TY,TZ in traslation.
            """

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

	def feasible_moves_selection(self, attractiveness_weight = self.attractiveness_weight, trails_weight = self.trails_weight):
		""" statistically select wich of the feasible move is the right one to select 
            attractivness is the 'a priori' desiderability of that move
            trail level   is the 'a posteriori' desiderability of that move
            """

		# memorize all evaluated position with respective fitness 
		evaluated_positions = list()
		most_feasible = (0,0,0,0) 
		numerator = denominator = 0 

        # for each move:
        # compute what happen with rotation and traslation in respect to fitness
		for move in self.feasible_moves:

			# set from where the object is located 
			gt = geometric_trasformation.geometric_trasformation(self.actual_position[0], self.actual_position[1], self.actual_position[2])

			# compute what the actual choice do to the object position 
			evaluated_position = gt.rototraslate_on_all_axis(move[0], move[1], move[2], move[3], move[4], move[5])

			# compute the attractivness of that move (a priory move ) 
			a_priory_desiderability = self.compute_fitness(evaluated_position)
			
			# compute trail level on this particular move ( a posteriori move ) 
			# TODO: function trails that return value of the trails level 
			a_posteriori_desiderability = self.trails(evaluated_position)

			# add to evaluted position every choice with it's respective fitness
			evaluated_positions.append((evaluated_position, a_priory_desiderability, a_posteriori_desiderability))

		# Compute probability of a move

		# first compute denominator 
		for position in evaluated_position:

			# retr previous stored data 
			a_priory_desiderability = position[1]
			a_posteriori_desiderability = position[2]

			denominator += (1 - attractiveness_weight) * a_priory_desiderability + trails_weight * a_posteriori_desiderability

        # then compute the probability 
		for position in evaluated_position:
			numerator = (1 - attractiveness_weight) * a_priory_desiderability + trails_weight * a_posteriori_desiderability

        	# compute the probability of that move 
			position_probability = numerator / denominator

			# chose the most feasible move
			if most_feasible[4] < position_probability:
				most_feasible = position + (position_probability)

		# return the most feasible move 
		return most_feasible

	def move(self):
		""" compute a set of feasible move, chose one of that, update the trails values 
			and finnaly add the move the the current solution 
		"""
		# create a set of feasible moves with a random approach
		self.feasible_moves_creation()

		# chose the best move in probability 
		selected_move = self.feasible_moves_selection()

		# update the trails
		self.trails.update(selected_move)

		# Append the move to the moves computed to create a complete solution
		self.selected_moves.append(selected_move)

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

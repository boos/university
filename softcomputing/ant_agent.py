#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
import threading, csv

import numpy as np
import random

import geometric_transformation
import trails

# SubClass of Thread Class 
class ANT(threading.Thread):
	""" ANT class. """

	STARTING_POSITION = np.array([[0],[0],[0]])

	# available rotation moves from 0 to 360 
	# available translation moves from -10.0 to +10.0 with 0.1 steps
	AVAILABLE_ROTATION_MOVES = np.arange(0,360)
	AVAILABLE_TRASLATION_MOVES = np.arange(-10,+10.1,0.1)

	# list that contains temporary feasible moves
	FEASIBLE_MOVES_SIZE = 30
	feasible_moves = list()

	# list with all the selected computed moves
	selected_moves = list() 

	def __init__(self, camerafilepath, real_position, trails, attr_weight, trails_weight):
		""" Initialize the first step of the  partial solution 
        
            Set also the coefficient weight of trail with respect to attractivness """

		# store local CSV file path 
		self.camerafilepath = camerafilepath

		# All ANT will start to explore solution from the origin
		self.selected_moves.append(self.STARTING_POSITION)
		self.actual_position = (0,0,0)

		# Store locally whate is the real position of the object in the space .
		self.real_position = real_position

		# store locally the reference to the trails 
		self.trails = trails

		# store locally attr_weight and trail_weight 
		self.attractiveness_weight = attr_weight
		self.trails_weight = trails_weight


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

	def feasible_moves_selection(self, attractiveness_weight = None, trails_weight = None):
		""" statistically select wich of the feasible move is the right one to select 
            attractivness is the 'a priori' desiderability of that move
            trail level   is the 'a posteriori' desiderability of that move
            """

		# set default value if not otherwise fixed
		if attractiveness_weight == None:
			attractiveness_weight = self.attractiveness_weight

		if trails_weight == None:
			trails_weight = self.trails_weight

		# memorize all evaluated position with respective fitness and trail level
		evaluated_positions = list()
		most_feasible = (0,0,0,0) 
		numerator = denominator = 0 

        # for each move:
		for move in self.feasible_moves:

			# set from where the object is located 
			gt = geometric_transformation.geometric_transformation(self.actual_position[0], self.actual_position[1], self.actual_position[2])

			# compute what the actual choice do to the object position 
			evaluated_position = gt.rototraslate_on_all_axis(move[0], move[1], move[2], move[3], move[4], move[5])

			# compute the attractivness of that move (a priory move ) 
			a_priory_desiderability = self.compute_fitness(evaluated_position)
			print "a_priory_desiderability:", a_priory_desiderability
			
			# compute trail level on this particular move ( a posteriori move ) using hints from others ANT's
			a_posteriori_desiderability = self.trails.value(evaluated_position)
			print "a_posteriori_desiderability:", a_posteriori_desiderability

			# add to evaluted position every choice with it's respective fitness
			evaluated_positions.append((evaluated_position, a_priory_desiderability, a_posteriori_desiderability))

		# Compute now in probability how good are the choices 

        # First we need the denominator value 
		for position in evaluated_positions:

			# for every evaluated position get previous calculated values 
			a_priory_desiderability = position[1]
			a_posteriori_desiderability = position[2]

            # compute denominator 
			denominator += (1 - attractiveness_weight) * a_priory_desiderability + (trails_weight * a_posteriori_desiderability)

        # Then we need to compute numerator and get data in probability 
		for position in evaluated_position:
			numerator = (1 - attractiveness_weight) * a_priory_desiderability + trails_weight * a_posteriori_desiderability

            # NOTE: I've skiped tabu list exclusion to evaluate the probability of a move using it in move creation 
            # using a short term tabu list task 

        	# compute the probability of that move 
			position_probability = numerator / denominator

			print "most_feasible:", most_feasible

			# As choice are created, memorize the best one ! 
			if most_feasible[3] < position_probability:
				most_feasible = position + (position_probability)

		# return the best feasible move 
		return most_feasible

	def move(self):
		""" compute a set of feasible move, chose one of that and finnaly add the move the the current solution 

            In ACO slides that is a creation of a state
		"""
		# create a set of feasible moves with a random approach
		self.feasible_moves_creation()

		# chose the best move in probability from set of moves created in feasible_moves_selection()
		self.actual_position = self.feasible_moves_selection()

		# Append the move to the moves computed to create a complete solution
		self.selected_moves.append(self.actual_position)

		return self.actual_position

    # show stats about current value of the camera error and distance from optimal selection 
	def stats(self, camera, camera_correction):
		print "STATS WILL BE HERE"




	# threading method called when ANT thread is started. 
	def run(self):
		camera = geometric_transformation.geometric_transformation(0,0,0)

		# open CSV file 
		with open(self.camerafilepath, 'r') as cameracsv:
			
			for line in csv.reader(cameracsv, skipinitialspace=True):
				
				# skip row with comments or empty
				if len(row) == 0: continue
				if row[0][0] == '#': continue

				# transform text to integers
				row = map(lambda x: float(x), row)

                # compute fix to errors 
				camera_correction = self.move()

                # apply fix to error 
                camera.rotate_X_axis(line[0] + line[1] - camera_correction[0])
                camera.rotate_Y_axis(line[2] + line[3] - camera_correction[1])
                camera.rotate_Z_axis(line[4] + line[5] - camera_correction[2])
                camera.traslate(line[6] + line[7] - camera_correction[3], line[8] + line[9] - camera_correction[4], line[10] + line[11] - camera_correction[5])

                # show stats about the current value and distance from corrections 
                self.stats(line, camera_correction)

		cameracsv.close()

        # Out of thread and when all other ANT's have computed a solution update the trail 

def testunit():
	
	atomic_ant = ANT("data/camera_rotations", (0,0,0), trails.trails(0.3,0.4), 0.1, 0.2)
	# feasible_moves_creation and feasible_moves_selection() do a complete move()
	#atomic_ant.feasible_moves_creation()
	#atomic_ant.feasible_moves_selection()

	print atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()
	atomic_ant.move()

	print atomic_ant.selected_moves

if __name__ == "__main__":
        testunit()

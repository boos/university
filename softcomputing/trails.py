#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import thread

class trails:
    """ Trails are updated at each interation of the alghorithm, 
        increasing the level of those related to moves that were part of 'good' solutions, 
        while decreasing all others. 

        After each iteration t of the algorithm, trails are updated
        using the following formula.

        ÃÂ ÃÂ¹ÃÂ (t ) = ÃÂÃÂÃÂ¹ÃÂ (t Ã¢ÂÂ 1) + Ã¢ÂÂÃÂ ÃÂ¹ÃÂ

        where ÃÂ is a user-defined evaporation coefficient and
        Ã¢ÂÂÃÂÃÂ¹ÃÂ represents the sum of the contributions of all ants
        that used move (ÃÂ¹ÃÂ) to construct their solution.

        As iteration I mean after each set of ANTs have computed a solution.
        So at every algorithms interation first of all decrease all the value on the TRAILS. 
        Then for every ANT, increase the trails 
        For every ANT:
        - decrease first of all all the value of the TRAILS and th

        """

    # initialize a 3D matrix with all the moves of previous ANTs 
    def __init__(s, evaporation_coefficient, pherormone_constant):

        # create ADT for memorize trails 
        s.trails = dict()

        # Store evaporation coefficient of the pherormone 
        s.evaporation_coefficient = evaporation_coefficient

        # Store of how much every ANT increase pherormone trails when use a path 
        s.pherormone_constant = pherormone_constant 


    def evaporation_action(s):
        """ Decrease globally all the trails 
		
		After earch iterazion of the algorithm the pherormone evaporate. 
		This is the method that handled this step. 
		"""

        for x in trails:
            for y in trails[x]:
                for z in trails[x][y]:
                    trails[x][y][z] = s.evaporation_coefficient * trails[x][y][z]


    
    def update(s, selected_ant_moves, solution_length):
        """ Increase trails used by single ANT 

			After earch iteration of the algorithm the pherormone evaporate but the path used by ANTS gets new pherormone.
			This is the method that handle this step.
            
            For every moves the ANT have done increase the trails on that path 
            Trails are increase with value of Q/L . 
            Q is a constant, L is the length of the complete solution """

        for selected_move in selected_ant_moves:

            x = selected_move[0]
            y = selected_move[1]
            z = selected_move[2]

            if not s.trails.has_key(x):
                s.trails[x] = dict()
    
            if not s.trails[x].has_key(y):
                s.trails[x][y] = dict()

            if not s.trails[x][y].has_key(z):
                s.trails[x][y][z] = 0

			# increase path used by ants 
            s.trails[x][y][z] = s.pherormone_constant / solution_length


    def value(s, selected_move):
        """ return trails value of a path """

        value = 0 

        x = selected_move[0][0]
        y = selected_move[1][0]
        z = selected_move[2][0]

        if s.trails.has_key(x):
            if s.trails[x].has_ke(y):
                if s.trails[x][y].has_key(z):
                    value = s.trails[x][y][z]

        return value

def testunit():
    


if __name__ == "__main__":
      testunit()
